#!/usr/bin/env python3
"""
Recalculate ModExp analysis with updated EIP-7883 formula
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from eip7883_analysis import ModExpGasCalculator, recalculate_costs
from utils import enrich_with_transaction_data, analyze_gas_usage_patterns, identify_affected_protocols

def main():
    print("Loading existing data...")
    df = pd.read_parquet('analysis_output/modexp_analysis_data.parquet')
    print(f"Loaded {len(df):,} ModExp calls")
    
    # Backup original costs
    df['eip2565_cost_orig'] = df['eip2565_cost']
    df['eip7883_cost_orig'] = df['eip7883_cost']
    df['cost_increase_orig'] = df['cost_increase']
    
    print("\nRecalculating costs with updated EIP-7883 formula...")
    df = recalculate_costs(df)
    
    # Update main columns with new calculations
    df['eip2565_cost'] = df['eip2565_cost_new']
    df['eip7883_cost'] = df['eip7883_cost_new']
    df['cost_increase'] = df['cost_increase_new']
    df['cost_ratio'] = df['cost_ratio_new']
    
    # Recalculate ETH costs if gas_price is available
    if 'gas_price' in df.columns:
        df['eth_cost_current'] = df['eip2565_cost'] * df['gas_price'] / 1e18
        df['eth_cost_eip7883'] = df['eip7883_cost'] * df['gas_price'] / 1e18
        df['eth_cost_increase'] = df['eth_cost_eip7883'] - df['eth_cost_current']
    
    print("\nComparison of calculations:")
    print(f"Original formula - Calls with increase: {(df['cost_increase_orig'] > 0).sum():,}")
    print(f"Updated formula - Calls with increase: {(df['cost_increase'] > 0).sum():,}")
    
    print("\nSample comparisons:")
    sample = df[df['cost_increase'] > 0].head(5)
    for idx, row in sample.iterrows():
        print(f"B={row['Bsize']}, E={row['Esize']}, M={row['Msize']}:")
        print(f"  Original: EIP-2565={row['eip2565_cost_orig']}, EIP-7883={row['eip7883_cost_orig']}, Increase={row['cost_increase_orig']}")
        print(f"  Updated:  EIP-2565={row['eip2565_cost']}, EIP-7883={row['eip7883_cost']}, Increase={row['cost_increase']}")
    
    # Save updated data
    print("\nSaving updated analysis data...")
    df.to_parquet('analysis_output/modexp_analysis_data_updated.parquet')
    
    # Generate summary statistics
    summary_stats = {
        'total_calls': len(df),
        'unique_transactions': df['tx_hash'].nunique(),
        'calls_with_increase': (df['cost_increase'] > 0).sum(),
        'pct_calls_affected': 100 * (df['cost_increase'] > 0).sum() / len(df),
        'total_cost_increase': df['cost_increase'].sum(),
        'avg_cost_increase': df[df['cost_increase'] > 0]['cost_increase'].mean() if (df['cost_increase'] > 0).any() else 0,
        'median_cost_increase': df[df['cost_increase'] > 0]['cost_increase'].median() if (df['cost_increase'] > 0).any() else 0,
        'max_cost_increase': df['cost_increase'].max(),
        'block_range': f"{df['block_number'].min()}-{df['block_number'].max()}"
    }
    
    print("\nSummary Statistics:")
    for key, value in summary_stats.items():
        print(f"{key}: {value}")
    
    # Save summary
    with open('analysis_output/analysis_summary_updated.txt', 'w') as f:
        for key, value in summary_stats.items():
            f.write(f"{key}: {value}\n")
    
    print("\nAnalysis complete!")
    return df, summary_stats

if __name__ == "__main__":
    df, stats = main()