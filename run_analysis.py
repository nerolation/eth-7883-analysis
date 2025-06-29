#!/usr/bin/env python3
"""
Main script to run EIP-7883 analysis with transaction enrichment
"""

import os
import sys
import argparse
from pathlib import Path
import pandas as pd
import pyxatu

from eip7883_analysis import ModExpDataAnalyzer, generate_report
from utils import enrich_with_transaction_data, analyze_gas_usage_patterns, identify_affected_protocols, export_summary_stats


def main():
    parser = argparse.ArgumentParser(description="Run comprehensive EIP-7883 ModExp analysis")
    parser.add_argument("--data-dir", type=str, default="modexp/modexp", 
                       help="Directory containing ModExp parquet files")
    parser.add_argument("--output-dir", type=str, default="analysis_output",
                       help="Output directory for results")
    parser.add_argument("--limit", type=int, help="Limit number of files to process")
    parser.add_argument("--enrich-txs", action="store_true", 
                       help="Enrich with transaction data from Xatu")
    parser.add_argument("--quick", action="store_true",
                       help="Quick analysis with limited data")
    
    args = parser.parse_args()
    
    # Create output directory
    output_path = Path(args.output_dir)
    output_path.mkdir(exist_ok=True)
    
    print("=== EIP-7883 ModExp Gas Cost Analysis ===\n")
    
    # Initialize analyzer
    print(f"Loading data from: {args.data_dir}")
    analyzer = ModExpDataAnalyzer(args.data_dir)
    
    # Load ModExp data
    limit = 100 if args.quick else args.limit
    df = analyzer.load_modexp_data(limit=limit)
    
    print(f"\nData loaded successfully:")
    print(f"- Total calls: {len(df):,}")
    print(f"- Unique transactions: {df['tx_hash'].nunique():,}")
    print(f"- Block range: {df['block_number'].min():,} to {df['block_number'].max():,}")
    
    # Enrich with transaction data if requested
    if args.enrich_txs:
        print("\nEnriching with transaction data...")
        try:
            xatu = pyxatu.PyXatu()
            analyzer.df = enrich_with_transaction_data(analyzer.df, xatu)
            print("Transaction data enrichment complete")
        except Exception as e:
            print(f"Warning: Could not enrich with transaction data: {e}")
    
    # Analyze gas usage patterns
    print("\nAnalyzing gas usage patterns...")
    patterns = analyze_gas_usage_patterns(analyzer.df)
    
    print(f"\nTop parameter combinations:")
    print(patterns["top_param_combos"].head(10))
    
    print(f"\nFermat prime usage: {patterns['fermat_usage']['count']:,} calls ({patterns['fermat_usage']['percentage']:.1f}%)")
    
    print(f"\nSize statistics:")
    for param, stats in patterns["size_stats"].items():
        print(f"  {param}: mean={stats['mean']:.1f}, median={stats['median']:.0f}, p95={stats['p95']:.0f}, max={stats['max']}")
    
    # Create visualizations
    print("\nGenerating visualizations...")
    analyzer.create_visualizations(args.output_dir)
    
    # Export summary statistics
    export_summary_stats(analyzer.df, output_path / "summary_statistics.csv")
    
    # Identify affected protocols if we have transaction data
    if "to_address" in analyzer.df.columns:
        print("\nIdentifying most affected protocols...")
        affected_protocols = identify_affected_protocols(analyzer.df)
        affected_protocols.head(20).to_csv(output_path / "affected_protocols.csv")
        print(f"Top affected protocols saved to affected_protocols.csv")
    
    # Generate comprehensive report
    print("\nGenerating analysis report...")
    generate_report(analyzer, output_path / "eip7883_analysis_report.md")
    
    # Quick summary
    print("\n=== Analysis Summary ===")
    total_calls = len(analyzer.df)
    affected_calls = (analyzer.df["cost_increase"] > 0).sum()
    pct_affected = 100 * affected_calls / total_calls
    avg_increase = analyzer.df["cost_increase"].mean()
    max_increase = analyzer.df["cost_increase"].max()
    
    print(f"Total ModExp calls analyzed: {total_calls:,}")
    print(f"Calls with cost increase: {affected_calls:,} ({pct_affected:.1f}%)")
    print(f"Average cost increase: {avg_increase:.0f} gas")
    print(f"Maximum cost increase: {max_increase:,} gas")
    print(f"\nDetailed results saved to: {args.output_dir}/")
    

if __name__ == "__main__":
    main()