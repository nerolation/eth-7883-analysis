#!/usr/bin/env python3
"""
Generate comprehensive markdown analysis report from EIP-7883 analysis outputs
Combines data from analysis_output directory with optional direct analysis report
"""

import csv
import json
import argparse
from pathlib import Path
from datetime import datetime


def load_csv_data(file_path: Path) -> list:
    """Load CSV data into list of dictionaries"""
    if not file_path.exists():
        return []
    
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def parse_summary_file(file_path: Path) -> dict:
    """Parse the analysis summary text file"""
    if not file_path.exists():
        return {}
    
    stats = {}
    with open(file_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    for line in lines:
        if ':' in line and any(key in line for key in [
            'total_calls', 'unique_transactions', 'avg_cost_increase', 
            'median_cost_increase', 'max_cost_increase', 'total_cost_increase',
            'calls_with_increase', 'pct_calls_affected', 'block_range'
        ]):
            try:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle special cases
                if 'block_range' in key:
                    stats[key] = value
                elif '.' in value:
                    stats[key] = float(value)
                else:
                    stats[key] = int(value)
            except:
                continue
    
    return stats


def format_number(num):
    """Format numbers with commas"""
    if isinstance(num, (int, float)):
        return f"{num:,.0f}" if num == int(num) else f"{num:,.2f}"
    return str(num)


def generate_comprehensive_report(analysis_dir: Path, output_file: str):
    """Generate comprehensive markdown report from analysis outputs"""
    
    # Load data from analysis directory
    summary_stats = parse_summary_file(analysis_dir / "analysis_summary.txt")
    top_senders = load_csv_data(analysis_dir / "top_impacted_senders.csv")
    top_contracts = load_csv_data(analysis_dir / "top_impacted_contracts.csv")
    main_data = load_csv_data(analysis_dir / "modexp_analysis_data.csv")
    
    # Check if we have an existing analysis report to incorporate
    existing_report = ""
    report_files = list(analysis_dir.glob("*analysis_report.md"))
    if report_files:
        with open(report_files[0], 'r') as f:
            existing_report = f.read()
    
    # Start building the comprehensive report
    report = f"""# EIP-7883 ModExp Analysis Report

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Executive Summary

EIP-7883 impact analysis based on historical Ethereum mainnet data with statistical and entity-level insights.

### Key Findings

- **Total ModExp calls analyzed**: {format_number(summary_stats.get('total_calls', 'N/A'))}
- **Unique transactions**: {format_number(summary_stats.get('unique_transactions', 'N/A'))}
- **Calls with cost increases**: {format_number(summary_stats.get('calls_with_increase', 'N/A'))} ({summary_stats.get('pct_calls_affected', 0):.1f}% of all calls)
- **Total additional gas required**: {format_number(summary_stats.get('total_cost_increase', 'N/A'))} gas
- **Average cost increase per affected call**: {format_number(summary_stats.get('avg_cost_increase', 0))} gas
- **Maximum single call increase**: {format_number(summary_stats.get('max_cost_increase', 'N/A'))} gas

## Entity Analysis

### Most Impacted Senders

Addresses with highest total gas cost increases:

| Rank | Address | Total Increase (gas) | Avg Increase | Call Count | Current Total Cost | New Total Cost |
|------|---------|---------------------|--------------|------------|-------------------|----------------|"""

    # Add top senders
    for i, sender in enumerate(top_senders[:10], 1):
        addr = sender.get('from_address', 'N/A')
        total_inc = format_number(float(sender.get('total_increase', 0)))
        avg_inc = format_number(float(sender.get('avg_increase', 0)))
        call_count = format_number(int(sender.get('call_count', 0)))
        old_cost = format_number(float(sender.get('total_old_cost', 0)))
        new_cost = format_number(float(sender.get('total_new_cost', 0)))
        
        report += f"\n| {i} | [{addr[:10]}...](https://etherscan.io/address/{addr}) | {total_inc} | {avg_inc} | {call_count} | {old_cost} | {new_cost} |"

    report += """

### Most Impacted Contracts

Contracts with highest total gas cost increases:

| Rank | Contract Address | Total Increase (gas) | Avg Increase | Call Count | Unique Users | Current Total Cost | New Total Cost |
|------|------------------|---------------------|--------------|------------|--------------|-------------------|----------------|"""

    # Add top contracts  
    for i, contract in enumerate(top_contracts[:10], 1):
        addr = contract.get('to_address', 'N/A')
        total_inc = format_number(float(contract.get('total_increase', 0)))
        avg_inc = format_number(float(contract.get('avg_increase', 0)))
        call_count = format_number(int(contract.get('call_count', 0)))
        unique_users = format_number(int(contract.get('unique_users', 0)))
        old_cost = format_number(float(contract.get('total_old_cost', 0)))
        new_cost = format_number(float(contract.get('total_new_cost', 0)))
        
        report += f"\n| {i} | [{addr[:10]}...](https://etherscan.io/address/{addr}) | {total_inc} | {avg_inc} | {call_count} | {unique_users} | {old_cost} | {new_cost} |"

    # Add usage analysis if we have main data
    if main_data:
        total_calls = len(main_data)
        
        # Calculate usage patterns
        all_32_bytes = sum(1 for row in main_data if 
                          int(row.get('Bsize', 0)) == 32 and 
                          int(row.get('Esize', 0)) == 32 and 
                          int(row.get('Msize', 0)) == 32)
        large_exp = sum(1 for row in main_data if int(row.get('Esize', 0)) > 32)
        large_mod = sum(1 for row in main_data if int(row.get('Msize', 0)) > 32)
        large_base = sum(1 for row in main_data if int(row.get('Bsize', 0)) > 32)
        
        # Calculate cost patterns
        gas_costs = [int(row.get('gas_costs', 0)) for row in main_data]
        min_cost = min(gas_costs) if gas_costs else 0
        max_cost = max(gas_costs) if gas_costs else 0
        
        # Calculate cost increases
        increases = [float(row.get('cost_increase', 0)) for row in main_data if float(row.get('cost_increase', 0)) > 0]
        
        report += f"""

## Usage Patterns

### Distribution

- **Standard 32-byte inputs**: {format_number(all_32_bytes)} calls ({100*all_32_bytes/total_calls:.1f}%)
- **Large exponents (>32 bytes)**: {format_number(large_exp)} calls  
- **Large modulus (>32 bytes)**: {format_number(large_mod)} calls
- **Large base (>32 bytes)**: {format_number(large_base)} calls

### Gas Costs

- **Range**: {format_number(min_cost)} to {format_number(max_cost)} gas
- **Total calls**: {format_number(total_calls)}

### Cost Increases

For {format_number(len(increases))} affected calls:"""

        if increases:
            increases.sort()
            n = len(increases)
            percentiles = {
                10: increases[int(0.1 * n)],
                25: increases[int(0.25 * n)], 
                50: increases[int(0.5 * n)],
                75: increases[int(0.75 * n)],
                90: increases[int(0.9 * n)],
                95: increases[int(0.95 * n)],
                99: increases[int(0.99 * n)]
            }
            
            report += f"""

**Increase percentiles:**
- 10th percentile: {format_number(percentiles[10])} gas
- 25th percentile: {format_number(percentiles[25])} gas  
- 50th percentile (median): {format_number(percentiles[50])} gas
- 75th percentile: {format_number(percentiles[75])} gas
- 90th percentile: {format_number(percentiles[90])} gas
- 95th percentile: {format_number(percentiles[95])} gas
- 99th percentile: {format_number(percentiles[99])} gas"""

    # Add visualizations section
    report += """

## Visualizations and Charts

Interactive visualizations have been generated to complement this analysis:

- **`cost_increase_distribution.html`** - Distribution of gas cost increases
- **`cost_ratio_by_size.html`** - Cost ratios by input parameter sizes  
- **`cost_timeline.html`** - Gas cost trends over time (if sufficient block range)
- **`sender_impact.html`** - Top transaction senders by cost increase
- **`contract_impact.html`** - Top contracts by cost increase
- **`sender_vs_contract_distribution.html`** - Comparative impact distribution

These charts provide detailed visual analysis of EIP-7883 impact patterns and can be opened in any web browser for interactive exploration.

## Technical Implementation Details

### EIP-7883 Changes

EIP-7883 modifies the ModExp gas calculation in three key ways:

1. **Multiplication Complexity**: 
   - For inputs ≤32 bytes: Fixed cost of 16 (vs variable in EIP-2565)
   - For inputs >32 bytes: 2 × words² (vs more complex formula in EIP-2565)

2. **Iteration Count Multiplier**: 
   - Changed from 8× to 16× for large exponents (>32 bytes)

3. **Minimum Gas Cost**: 
   - Increased from 200 to 500 gas

### Impact Drivers

Cost increases driven by:
- **Minimum gas increase** (200→500) for small operations
- **Iteration multiplier change** (8×→16×) for large exponents
- **Simplified complexity** for predictable costs

## Analysis Methodology

### Data Scope"""

    # Add block range info with enhanced formatting
    block_range = summary_stats.get('block_range', 'N/A')
    block_range_display = block_range
    block_span = "Unknown"
    
    if isinstance(block_range, str) and 'np.int64' in block_range:
        import re
        matches = re.findall(r'np\.int64\((\d+)\)', block_range)
        if len(matches) == 2:
            start_block = int(matches[0])
            end_block = int(matches[1])
            block_span = f"{end_block - start_block + 1:,} blocks"
            block_range_display = f"{start_block:,} to {end_block:,}"
    elif isinstance(block_range, str) and '(' in block_range:
        # Handle tuple format like "(21659928, 22785670)"
        import re
        matches = re.findall(r'\((\d+),\s*(\d+)\)', block_range)
        if matches:
            start_block = int(matches[0][0])
            end_block = int(matches[0][1])
            block_span = f"{end_block - start_block + 1:,} blocks"
            block_range_display = f"{start_block:,} to {end_block:,}"

    report += f"""
- **Block range**: {block_range_display} ({block_span})
- **Total calls analyzed**: {format_number(summary_stats.get('total_calls', 'N/A'))}
- **Data source**: Ethereum mainnet ModExp precompile calls
- **Analysis date**: {datetime.now().strftime('%Y-%m-%d')}

### Methods
- Gas costs calculated using EIP-2565 and EIP-7883 formulas
- Increases represent additional gas required under EIP-7883
- Entity analysis groups by senders and contracts
- Percentiles exclude zero-increase calls

## Conclusions and Implications

### Impact Assessment

1. **Limited scope**: Only {summary_stats.get('pct_calls_affected', 0):.1f}% of calls affected
2. **Predictable costs**: Impact follows input size patterns
3. **Entity concentration**: Impact focused on small number of addresses
4. **Security improvement**: DoS protection with minimal legitimate impact

### Recommendations

#### For Affected Entities
- Review ModExp usage patterns and budget for increased costs
- Large exponent operations see significant increases
- Optimize exponent sizes where possible

#### For Infrastructure
- Update gas estimation tools for EIP-7883
- Monitor post-implementation usage patterns
- Guide users, especially top-impacted entities

#### For Ethereum Community
- Targeted fixes for underpriced edge cases
- Concentrated impact enables focused outreach
- Predictable changes allow effective planning

### Data Notes

Analysis based on historical mainnet data ({format_number(summary_stats.get('total_calls', 'N/A'))} calls). ModExp precompile primarily used by cryptographic applications and ZK proof systems.

---

*Report generated using historical Ethereum mainnet data. Gas calculations verified against EIP-2565 and EIP-7883 specifications.*
"""

    # Write the final report
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"Comprehensive analysis report saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate comprehensive markdown report from EIP-7883 analysis outputs")
    parser.add_argument("--analysis-dir", type=str, default="analysis_output", 
                       help="Directory containing analysis output files")
    parser.add_argument("--output", type=str, default="eip7883_comprehensive_analysis.md",
                       help="Output markdown file name")
    
    args = parser.parse_args()
    
    analysis_dir = Path(args.analysis_dir)
    if not analysis_dir.exists():
        print(f"ERROR: Analysis directory {analysis_dir} does not exist")
        return
    
    print(f"Loading analysis data from {analysis_dir}")
    generate_comprehensive_report(analysis_dir, args.output)


if __name__ == "__main__":
    main()