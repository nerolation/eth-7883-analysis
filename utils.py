#!/usr/bin/env python3
"""
Utility functions for ModExp data processing
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Optional, Dict
import concurrent.futures
import pyxatu


def enrich_with_transaction_data(
    modexp_df: pd.DataFrame,
    xatu_client: Optional[pyxatu.PyXatu] = None,
    batch_size: int = 7200
) -> pd.DataFrame:
    """Enrich ModExp data with transaction metadata from Xatu"""
    
    if xatu_client is None:
        xatu_client = pyxatu.PyXatu()
        
    # Get unique blocks with ModExp calls
    modexp_blocks = set(modexp_df["block_number"].unique())
    modexp_txs = set(modexp_df["tx_hash"].unique())
    
    min_block = min(modexp_blocks)
    max_block = max(modexp_blocks)
    
    print(f"Fetching transaction data for blocks {min_block} to {max_block}")
    
    query_template = """
    SELECT 
        block_number, 
        transaction_hash as tx_hash, 
        from_address, 
        to_address, 
        value, 
        gas_used, 
        gas_price, 
        transaction_type 
    FROM canonical_execution_transaction
    WHERE meta_network_name = 'mainnet' 
        AND block_number >= {} 
        AND block_number < {}
    """
    
    tx_results = []
    
    for start_block in range(min_block, max_block + 1, batch_size):
        end_block = min(start_block + batch_size, max_block + 1)
        print(f"Querying blocks {start_block} to {end_block}")
        
        query = query_template.format(start_block, end_block)
        
        try:
            result = xatu_client.execute_query(
                query,
                columns="block_number, tx_hash, from_address, to_address, value, gas_used, gas_price, transaction_type"
            )
            
            # Filter to only ModExp transactions
            result = result[result["block_number"].isin(modexp_blocks)]
            result = result[result["tx_hash"].isin(modexp_txs)]
            
            if len(result) > 0:
                tx_results.append(result)
                
        except Exception as e:
            print(f"Error querying blocks {start_block}-{end_block}: {e}")
            
    if tx_results:
        tx_df = pd.concat(tx_results, ignore_index=True)
        
        # Merge with ModExp data
        enriched_df = pd.merge(
            modexp_df,
            tx_df,
            how="left",
            on=["block_number", "tx_hash"]
        )
        
        # Calculate ETH costs
        enriched_df["eth_cost_current"] = enriched_df["gas_costs"] * enriched_df["gas_price"] / 1e18
        enriched_df["eth_cost_eip7883"] = enriched_df["eip7883_cost"] * enriched_df["gas_price"] / 1e18
        enriched_df["eth_cost_increase"] = enriched_df["eth_cost_eip7883"] - enriched_df["eth_cost_current"]
        
        missing = enriched_df["from_address"].isna().sum()
        if missing > 0:
            print(f"WARNING: {missing} ModExp calls missing transaction data")
            
        return enriched_df
    else:
        print("No transaction data found")
        return modexp_df


def analyze_gas_usage_patterns(df: pd.DataFrame) -> Dict:
    """Analyze patterns in ModExp gas usage"""
    
    patterns = {}
    
    # Common parameter combinations
    param_combos = df.groupby(["Bsize", "Esize", "Msize"]).size().sort_values(ascending=False)
    patterns["top_param_combos"] = param_combos.head(20)
    
    # Exponent analysis
    df["exponent_int"] = df["E"].apply(lambda x: int(x, 16) if x else 0)
    df["is_fermat"] = df["exponent_int"].isin([3, 5, 17, 257, 65537])  # Common Fermat primes
    
    patterns["fermat_usage"] = {
        "count": df["is_fermat"].sum(),
        "percentage": 100 * df["is_fermat"].sum() / len(df)
    }
    
    # Size patterns
    patterns["size_stats"] = {
        "base": {
            "mean": df["Bsize"].mean(),
            "median": df["Bsize"].median(),
            "p95": df["Bsize"].quantile(0.95),
            "max": df["Bsize"].max()
        },
        "exponent": {
            "mean": df["Esize"].mean(),
            "median": df["Esize"].median(),
            "p95": df["Esize"].quantile(0.95),
            "max": df["Esize"].max()
        },
        "modulus": {
            "mean": df["Msize"].mean(),
            "median": df["Msize"].median(),
            "p95": df["Msize"].quantile(0.95),
            "max": df["Msize"].max()
        }
    }
    
    # Cost patterns
    patterns["cost_brackets"] = pd.cut(
        df["gas_costs"],
        bins=[0, 500, 1000, 5000, 10000, 50000, 100000, float('inf')],
        labels=["<500", "500-1k", "1k-5k", "5k-10k", "10k-50k", "50k-100k", ">100k"]
    ).value_counts()
    
    return patterns


def identify_affected_protocols(df: pd.DataFrame) -> pd.DataFrame:
    """Identify protocols/contracts most affected by EIP-7883"""
    
    if "to_address" not in df.columns:
        return pd.DataFrame()
        
    # Group by receiving contract
    contract_impact = df.groupby("to_address").agg({
        "cost_increase": ["sum", "mean", "count"],
        "from_address": "nunique",
        "gas_costs": "sum",
        "eip7883_cost": "sum"
    }).round(2)
    
    contract_impact.columns = [
        "total_increase", "avg_increase", "call_count",
        "unique_users", "total_current_cost", "total_new_cost"
    ]
    
    contract_impact["avg_cost_ratio"] = contract_impact["total_new_cost"] / contract_impact["total_current_cost"]
    
    return contract_impact.sort_values("total_increase", ascending=False)


def export_summary_stats(df: pd.DataFrame, output_file: str = "modexp_summary_stats.csv"):
    """Export summary statistics for further analysis"""
    
    summary = {
        "Total Calls": len(df),
        "Unique Transactions": df["tx_hash"].nunique(),
        "Block Range Start": df["block_number"].min(),
        "Block Range End": df["block_number"].max(),
        "Calls with Cost Increase": (df["cost_increase"] > 0).sum(),
        "Percent Affected": 100 * (df["cost_increase"] > 0).sum() / len(df),
        "Total Current Gas": df["gas_costs"].sum(),
        "Total EIP-7883 Gas": df["eip7883_cost"].sum(),
        "Total Gas Increase": df["cost_increase"].sum(),
        "Average Cost Increase": df["cost_increase"].mean(),
        "Median Cost Increase": df["cost_increase"].median(),
        "Max Cost Increase": df["cost_increase"].max(),
        "Calls with Base > 32": (df["Bsize"] > 32).sum(),
        "Calls with Exp > 32": (df["Esize"] > 32).sum(),
        "Calls with Mod > 32": (df["Msize"] > 32).sum()
    }
    
    summary_df = pd.DataFrame([summary]).T
    summary_df.columns = ["Value"]
    summary_df.to_csv(output_file)
    
    print(f"Summary statistics exported to {output_file}")
    
    return summary_df