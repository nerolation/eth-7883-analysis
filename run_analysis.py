#!/usr/bin/env python3
"""
Main script to run EIP-7883 analysis optimized for large datasets
"""

import os
import sys
import argparse
from pathlib import Path
import pandas as pd
import time

from eip7883_analysis import ModExpDataAnalyzer
from utils import enrich_with_transaction_data, analyze_gas_usage_patterns, identify_affected_protocols


def main():
    parser = argparse.ArgumentParser(description="Run comprehensive EIP-7883 ModExp analysis")
    parser.add_argument("--data-dir", type=str, default="modexp/modexp", 
                       help="Directory containing ModExp parquet files")
    parser.add_argument("--output-dir", type=str, default="analysis_output",
                       help="Output directory for results")
    parser.add_argument("--limit", type=int, help="Limit number of files to process")
    parser.add_argument("--batch-size", type=int, default=1000, help="Batch size for file processing")
    parser.add_argument("--enrich-txs", action="store_true", 
                       help="Enrich with transaction data from Xatu")
    parser.add_argument("--max-tx-blocks", type=int, default=10000, help="Max blocks for transaction enrichment")
    parser.add_argument("--tx-batch-size", type=int, default=50, help="Batch size for transaction queries")
    parser.add_argument("--quick", action="store_true",
                       help="Quick analysis with limited data")
    
    args = parser.parse_args()
    
    # Create output directory
    output_path = Path(args.output_dir)
    output_path.mkdir(exist_ok=True)
    
    print("=== EIP-7883 ModExp Analysis (Optimized for Large Datasets) ===\n")
    
    start_time = time.time()
    
    # Initialize analyzer
    print(f"Loading data from: {args.data_dir}")
    analyzer = ModExpDataAnalyzer(args.data_dir)
    
    # Load ModExp data
    limit = 100 if args.quick else args.limit
    load_start = time.time()
    df = analyzer.load_modexp_data(limit=limit, batch_size=args.batch_size)
    load_time = time.time() - load_start
    
    print(f"\nData loaded in {load_time:.1f} seconds:")
    print(f"- Total calls: {len(df):,}")
    print(f"- Unique transactions: {df['tx_hash'].nunique():,}")
    print(f"- Block range: {df['block_number'].min():,} to {df['block_number'].max():,}")
    
    # Enrich with transaction data if requested
    if args.enrich_txs:
        print(f"\nEnriching with transaction data (max {args.max_tx_blocks:,} blocks)...")
        enrich_start = time.time()
        try:
            import pyxatu
            xatu = pyxatu.PyXatu()
            analyzer.df = enrich_with_transaction_data(
                analyzer.df, 
                xatu, 
                batch_size=args.tx_batch_size,
                max_blocks=args.max_tx_blocks
            )
            enrich_time = time.time() - enrich_start
            print(f"Transaction data enrichment complete in {enrich_time:.1f} seconds")
        except ImportError:
            print("ERROR: pyxatu not available, skipping transaction enrichment")
        except Exception as e:
            print(f"Warning: Could not enrich with transaction data: {e}")
    
    # Perform analysis
    print("\nPerforming impact analysis...")
    analysis_start = time.time()
    results = analyzer.analyze_impact()
    analysis_time = time.time() - analysis_start
    
    print(f"\nAnalysis complete in {analysis_time:.1f} seconds:")
    print(f"- Calls with cost increase: {results['calls_with_increase']:,} ({results['pct_calls_affected']:.1f}%)")
    print(f"- Average cost increase: {results['avg_cost_increase']:.1f} gas")
    print(f"- Total additional gas: {results['total_cost_increase']:,}")
    
    # Export results
    print("\nExporting results...")
    export_start = time.time()
    
    # Save compressed data for large datasets
    analyzer.df.to_parquet(output_path / "modexp_analysis_data.parquet", compression="snappy")
    
    # Save CSV for smaller datasets
    if len(analyzer.df) < 100000:
        analyzer.df.to_csv(output_path / "modexp_analysis_data.csv", index=False)
    
    # Export summary
    with open(output_path / "analysis_summary.txt", "w") as f:
        f.write("EIP-7883 ModExp Analysis Summary\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Analysis completed: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total processing time: {time.time() - start_time:.1f} seconds\n\n")
        
        f.write("Performance:\n")
        f.write(f"  Data loading: {load_time:.1f}s\n")
        if args.enrich_txs:
            f.write(f"  Transaction enrichment: {enrich_time:.1f}s\n")
        f.write(f"  Analysis: {analysis_time:.1f}s\n\n")
        
        f.write("Results:\n")
        for key, value in results.items():
            if key != "top_impacted_addresses":
                f.write(f"  {key}: {value}\n")
    
    # Save entity analysis results if available
    if "top_impacted_senders" in results and results["top_impacted_senders"] is not None:
        results["top_impacted_senders"].to_csv(output_path / "top_impacted_senders.csv")
        
    if "top_impacted_contracts" in results and results["top_impacted_contracts"] is not None:
        results["top_impacted_contracts"].to_csv(output_path / "top_impacted_contracts.csv")
    
    # Perform enhanced entity analysis if transaction data available
    try:
        entity_results = analyzer.analyze_entities()
        if entity_results:
            print("Enhanced entity analysis completed")
            
            # Save detailed entity analysis
            if "sender_analysis" in entity_results:
                entity_results["sender_analysis"].to_csv(output_path / "detailed_sender_analysis.csv")
                print(f"- detailed_sender_analysis.csv")
                
            if "contract_analysis" in entity_results:
                entity_results["contract_analysis"].to_csv(output_path / "detailed_contract_analysis.csv") 
                print(f"- detailed_contract_analysis.csv")
                
            if "entity_patterns" in entity_results:
                patterns = entity_results["entity_patterns"]
                if "top_sender_contract_pairs" in patterns:
                    patterns["top_sender_contract_pairs"].to_csv(output_path / "sender_contract_pairs.csv")
                    print(f"- sender_contract_pairs.csv")
    except Exception as e:
        print(f"Enhanced entity analysis failed: {e}")
    
    export_time = time.time() - export_start
    total_time = time.time() - start_time
    
    print(f"Export completed in {export_time:.1f} seconds")
    print(f"\nTotal analysis time: {total_time:.1f} seconds")
    print(f"Results saved to {args.output_dir}/:")
    print(f"- modexp_analysis_data.parquet (compressed)")
    if len(analyzer.df) < 100000:
        print(f"- modexp_analysis_data.csv (readable)")
    print(f"- analysis_summary.txt (summary)")
    
    if "top_impacted_senders" in results:
        print(f"- top_impacted_senders.csv (sender analysis)")
    if "top_impacted_contracts" in results:
        print(f"- top_impacted_contracts.csv (contract analysis)")
    

if __name__ == "__main__":
    main()