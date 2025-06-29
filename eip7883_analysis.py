#!/usr/bin/env python3
"""
EIP-7883 ModExp Gas Cost Analysis
Empirical analysis of the impact of EIP-7883 on Ethereum network
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


class ModExpGasCalculator:
    """Calculate ModExp gas costs according to different EIP specifications"""
    
    @staticmethod
    def calculate_eip2565_cost(base_length: int, exponent_length: int, modulus_length: int, exponent_bytes: str) -> int:
        """Calculate gas cost according to EIP-2565 (current mainnet)"""
        exponent_int = int(exponent_bytes, 16) if exponent_bytes else 0
        max_length = max(base_length, modulus_length)
        words = (max_length + 7) // 8
        
        # Multiplication complexity
        if max_length <= 64:
            multiplication_complexity = words ** 2
        elif max_length <= 1024:
            multiplication_complexity = (words ** 2) // 4 + 96 * words - 3072
        else:
            multiplication_complexity = (words ** 2) // 16 + 480 * words - 199680
            
        # Iteration count
        if exponent_length <= 32:
            if exponent_int == 0:
                iteration_count = 0
            else:
                iteration_count = exponent_int.bit_length() - 1
        else:
            iteration_count = 8 * (exponent_length - 32)
            iteration_count += (exponent_int & (2**256 - 1)).bit_length() - 1
            
        iteration_count = max(iteration_count, 1)
        
        # Final gas cost
        return max(200, (multiplication_complexity * iteration_count) // 3)
    
    @staticmethod
    def calculate_eip7883_cost(base_length: int, exponent_length: int, modulus_length: int, exponent_bytes: str) -> int:
        """Calculate gas cost according to EIP-7883 (proposed)"""
        exponent_int = int(exponent_bytes, 16) if exponent_bytes else 0
        max_length = max(base_length, modulus_length)
        words = (max_length + 7) // 8
        
        # Multiplication complexity - NEW FORMULA
        if max_length <= 32:
            multiplication_complexity = 16
        else:
            multiplication_complexity = 2 * (words ** 2)
            
        # Iteration count - UPDATED MULTIPLIER
        if exponent_length <= 32:
            if exponent_int == 0:
                iteration_count = 0
            else:
                iteration_count = exponent_int.bit_length() - 1
        else:
            iteration_count = 16 * (exponent_length - 32)  # Changed from 8 to 16
            iteration_count += (exponent_int & (2**256 - 1)).bit_length() - 1
            
        iteration_count = max(iteration_count, 1)
        
        # Final gas cost - HIGHER MINIMUM
        return max(500, (multiplication_complexity * iteration_count) // 3)  # Changed from 200 to 500


class ModExpDataAnalyzer:
    """Analyze ModExp precompile usage data"""
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        if not self.data_dir.exists():
            raise ValueError(f"Data directory {data_dir} does not exist")
        
        self.df = None
        self.tx_data = None
        
    def load_modexp_data(self, limit: Optional[int] = None, batch_size: int = 1000) -> pd.DataFrame:
        """Load ModExp call data from parquet files with robust error handling"""
        print(f"Loading ModExp data from {self.data_dir}")
        
        parquet_files = sorted(
            self.data_dir.glob("*.parquet"),
            key=lambda x: int(x.stem),
            reverse=True
        )
        
        total_files = len(parquet_files)
        print(f"Found {total_files:,} parquet files")
        
        if limit and limit < total_files:
            parquet_files = parquet_files[:limit]
            print(f"Limited to {limit:,} files")
            
        dfs = []
        failed_files = []
        
        # Process files in batches to manage memory
        for batch_start in range(0, len(parquet_files), batch_size):
            batch_end = min(batch_start + batch_size, len(parquet_files))
            batch_files = parquet_files[batch_start:batch_end]
            
            print(f"Processing batch {batch_start//batch_size + 1}/{(len(parquet_files)-1)//batch_size + 1}: "
                  f"files {batch_start+1} to {batch_end} ({len(batch_files)} files)")
            
            batch_dfs = []
            for file in batch_files:
                try:
                    df = pd.read_parquet(file)
                    if len(df) > 0:  # Only include non-empty files
                        df["block_number"] = int(file.stem)
                        batch_dfs.append(df)
                except Exception as e:
                    print(f"WARNING: Failed to load {file.name}: {e}")
                    failed_files.append(file.name)
                    
            if batch_dfs:
                batch_df = pd.concat(batch_dfs, ignore_index=True)
                dfs.append(batch_df)
                
        if not dfs:
            raise ValueError("No valid ModExp data found")
            
        self.df = pd.concat(dfs, ignore_index=True)
        
        if failed_files:
            print(f"WARNING: Failed to load {len(failed_files)} files: {failed_files[:5]}...")
            
        print(f"Successfully loaded {len(self.df):,} ModExp calls from {len(parquet_files)-len(failed_files):,} blocks")
        
        # Calculate gas costs
        self._calculate_gas_costs()
        
        return self.df
    
    def _calculate_gas_costs(self):
        """Calculate both EIP-2565 and EIP-7883 gas costs"""
        print("Calculating gas costs...")
        
        # Current EIP-2565 costs (should match gas_costs column)
        self.df["eip2565_cost"] = self.df.apply(
            lambda row: ModExpGasCalculator.calculate_eip2565_cost(
                row["Bsize"], row["Esize"], row["Msize"], row["E"]
            ), axis=1
        )
        
        # Proposed EIP-7883 costs
        self.df["eip7883_cost"] = self.df.apply(
            lambda row: ModExpGasCalculator.calculate_eip7883_cost(
                row["Bsize"], row["Esize"], row["Msize"], row["E"]
            ), axis=1
        )
        
        # Calculate differences
        self.df["cost_increase"] = self.df["eip7883_cost"] - self.df["gas_costs"]
        self.df["cost_ratio"] = self.df["eip7883_cost"] / self.df["gas_costs"]
        
        # Verify our EIP-2565 implementation matches recorded gas costs
        mismatch = self.df[self.df["eip2565_cost"] != self.df["gas_costs"]]
        if len(mismatch) > 0:
            print(f"WARNING: {len(mismatch)} calls have mismatched EIP-2565 calculations")
            
    def load_transaction_data(self, tx_data_path: Optional[str] = None):
        """Load transaction metadata if available"""
        if tx_data_path and Path(tx_data_path).exists():
            self.tx_data = pd.read_parquet(tx_data_path)
            self.df = pd.merge(
                self.df, self.tx_data,
                how="left",
                on=["block_number", "tx_hash"]
            )
            
    def analyze_impact(self) -> dict:
        """Perform comprehensive impact analysis"""
        results = {}
        
        # Basic statistics
        results["total_calls"] = len(self.df)
        results["unique_transactions"] = self.df["tx_hash"].nunique()
        results["block_range"] = (self.df["block_number"].min(), self.df["block_number"].max())
        
        # Cost impact
        results["avg_cost_increase"] = self.df["cost_increase"].mean()
        results["median_cost_increase"] = self.df["cost_increase"].median()
        results["max_cost_increase"] = self.df["cost_increase"].max()
        results["total_cost_increase"] = self.df["cost_increase"].sum()
        
        # Affected calls
        results["calls_with_increase"] = len(self.df[self.df["cost_increase"] > 0])
        results["pct_calls_affected"] = 100 * results["calls_with_increase"] / results["total_calls"]
        
        # Size distribution
        results["calls_over_32_bytes"] = {
            "base": len(self.df[self.df["Bsize"] > 32]),
            "exponent": len(self.df[self.df["Esize"] > 32]),
            "modulus": len(self.df[self.df["Msize"] > 32])
        }
        
        # Address analysis if transaction data available
        if "from_address" in self.df.columns:
            address_impact = self.df.groupby("from_address").agg({
                "cost_increase": ["sum", "mean", "count"],
                "gas_costs": "sum",
                "eip7883_cost": "sum"
            }).round(2)
            
            address_impact.columns = ["total_increase", "avg_increase", "call_count", 
                                     "total_old_cost", "total_new_cost"]
            address_impact = address_impact.sort_values("total_increase", ascending=False)
            results["top_impacted_addresses"] = address_impact.head(20)
            
        return results
    
    def create_visualizations(self, output_dir: str = "output"):
        """Create analysis visualizations"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # 1. Cost increase distribution
        fig = px.histogram(
            self.df[self.df["cost_increase"] > 0],
            x="cost_increase",
            nbins=50,
            title="Distribution of Gas Cost Increases (EIP-7883)",
            labels={"cost_increase": "Gas Cost Increase", "count": "Number of Calls"}
        )
        fig.update_layout(yaxis_type="log")
        fig.write_html(output_path / "cost_increase_distribution.html")
        
        # 2. Cost ratio by input size
        fig = go.Figure()
        
        for size_col, name in [("Bsize", "Base"), ("Esize", "Exponent"), ("Msize", "Modulus")]:
            size_bins = pd.cut(self.df[size_col], bins=[0, 32, 64, 128, 256, 512, 1024, 2048, 4096])
            avg_ratio = self.df.groupby(size_bins)["cost_ratio"].mean()
            
            fig.add_trace(go.Bar(
                name=f"{name} Size",
                x=[str(b) for b in avg_ratio.index],
                y=avg_ratio.values
            ))
            
        fig.update_layout(
            title="Average Cost Ratio by Input Size",
            xaxis_title="Size Range (bytes)",
            yaxis_title="Cost Ratio (EIP-7883 / Current)",
            barmode='group'
        )
        fig.write_html(output_path / "cost_ratio_by_size.html")
        
        # 3. Timeline analysis
        if self.df["block_number"].nunique() > 100:
            daily_impact = self.df.groupby("block_number").agg({
                "cost_increase": "sum",
                "gas_costs": "sum",
                "eip7883_cost": "sum"
            }).rolling(window=7200).mean()  # ~1 day average
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=daily_impact.index,
                y=daily_impact["gas_costs"],
                name="Current Cost",
                line=dict(color="blue")
            ))
            fig.add_trace(go.Scatter(
                x=daily_impact.index,
                y=daily_impact["eip7883_cost"],
                name="EIP-7883 Cost",
                line=dict(color="red")
            ))
            fig.update_layout(
                title="ModExp Gas Costs Over Time (7200 block average)",
                xaxis_title="Block Number",
                yaxis_title="Gas Cost"
            )
            fig.write_html(output_path / "cost_timeline.html")
            
        # 4. Address impact (if available)
        if "from_address" in self.df.columns:
            address_stats = self.df.groupby("from_address").agg({
                "cost_increase": "sum",
                "tx_hash": "count"
            }).sort_values("cost_increase", ascending=False).head(20)
            
            fig = px.bar(
                address_stats.reset_index(),
                x="from_address",
                y="cost_increase",
                title="Top 20 Addresses by Total Cost Increase",
                labels={"cost_increase": "Total Cost Increase", "from_address": "Address"}
            )
            fig.update_xaxes(tickangle=45)
            fig.write_html(output_path / "address_impact.html")
            
        print(f"Visualizations saved to {output_path}")


def generate_report(analyzer: ModExpDataAnalyzer, output_file: str = "eip7883_analysis_report.md"):
    """Generate a professional analysis report"""
    results = analyzer.analyze_impact()
    
    report = f"""# EIP-7883 ModExp Gas Cost Analysis Report

## Executive Summary

This report analyzes the empirical impact of EIP-7883 on ModExp precompile usage based on {results['total_calls']:,} historical calls across {results['unique_transactions']:,} transactions.

### Key Findings

- **Total calls analyzed**: {results['total_calls']:,}
- **Calls with cost increase**: {results['calls_with_increase']:,} ({results['pct_calls_affected']:.1f}%)
- **Average cost increase**: {results['avg_cost_increase']:.0f} gas
- **Maximum cost increase**: {results['max_cost_increase']:,} gas
- **Total additional gas**: {results['total_cost_increase']:,}

## Detailed Analysis

### 1. Cost Impact Distribution

The gas cost increases under EIP-7883 vary significantly based on input parameters:

- **Median increase**: {results['median_cost_increase']:.0f} gas
- **Average increase**: {results['avg_cost_increase']:.0f} gas
- **Maximum increase**: {results['max_cost_increase']:,} gas

### 2. Input Size Analysis

Calls with inputs over 32 bytes (most affected by EIP-7883):
- Base > 32 bytes: {results['calls_over_32_bytes']['base']:,} calls
- Exponent > 32 bytes: {results['calls_over_32_bytes']['exponent']:,} calls  
- Modulus > 32 bytes: {results['calls_over_32_bytes']['modulus']:,} calls

### 3. Network Impact

Based on the analyzed data:
- Block range: {results['block_range'][0]:,} to {results['block_range'][1]:,}
- Average additional gas per block: {results['total_cost_increase'] / (results['block_range'][1] - results['block_range'][0]):.0f}

"""

    if "top_impacted_addresses" in results:
        report += """### 4. Most Impacted Addresses

| Address | Total Increase | Avg Increase | Call Count |
|---------|---------------|--------------|------------|
"""
        for addr, row in results["top_impacted_addresses"].head(10).iterrows():
            report += f"| `{addr[:10]}...` | {row['total_increase']:,.0f} | {row['avg_increase']:,.0f} | {row['call_count']:,} |\n"

    report += """
## Conclusions

1. **Limited Impact**: Only {:.1f}% of ModExp calls see cost increases under EIP-7883.

2. **Targeted Changes**: The increases primarily affect calls with large inputs (>32 bytes), which aligns with EIP-7883's goal of addressing underpriced edge cases.

3. **Security Improvement**: The minimum cost increase from 200 to 500 gas provides better protection against potential DoS attacks using small inputs.

4. **Predictable Impact**: The cost increases follow a predictable pattern based on input sizes, allowing users to estimate impacts.

## Recommendations

1. **Contract Operators**: Review ModExp usage patterns and budget for potential gas increases, particularly for operations with large exponents.

2. **Network Monitoring**: Continue monitoring ModExp usage patterns post-implementation to validate impact estimates.

3. **Documentation**: Update documentation and tools to reflect new gas calculations for developer awareness.
""".format(results['pct_calls_affected'])

    with open(output_file, "w") as f:
        f.write(report)
        
    print(f"Report saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Analyze EIP-7883 ModExp gas cost impact")
    parser.add_argument("--data-dir", type=str, required=True, help="Directory containing ModExp parquet files")
    parser.add_argument("--tx-data", type=str, help="Optional transaction data parquet file")
    parser.add_argument("--output-dir", type=str, default="output", help="Output directory for results")
    parser.add_argument("--limit", type=int, help="Limit number of files to process")
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = ModExpDataAnalyzer(args.data_dir)
    
    # Load data
    analyzer.load_modexp_data(limit=args.limit)
    
    # Load transaction data if available
    if args.tx_data:
        analyzer.load_transaction_data(args.tx_data)
        
    # Create visualizations
    analyzer.create_visualizations(args.output_dir)
    
    # Generate report
    report_path = os.path.join(args.output_dir, "eip7883_analysis_report.md")
    generate_report(analyzer, report_path)
    
    print(f"\nAnalysis complete! Results saved to {args.output_dir}/")


if __name__ == "__main__":
    main()