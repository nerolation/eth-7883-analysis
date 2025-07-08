# EIP-7883 ModExp Gas Cost Analysis

Comprehensive empirical analysis of EIP-7883's impact on Ethereum's ModExp precompile gas costs, featuring detailed entity-level analysis and sophisticated statistical insights.

## Overview

EIP-7883 proposes changes to the ModExp precompile pricing to address underpricing in certain edge cases. This repository provides multiple analysis tools to examine historical ModExp usage and quantify the impact of these changes.

### Key Changes in EIP-7883:
- Minimum gas cost increased from 200 to 500
- Exponent length cost multiplier increased from 8 to 16  
- Modified multiplication complexity calculation

### Analysis Highlights:
- **304,301 ModExp calls analyzed** from Ethereum mainnet
- **38.5% of calls affected** with average 116 gas increase
- **Detailed entity analysis** with top 50 most affected addresses
- **Interactive visualizations** for impact exploration

## Quick Start

### Large-Scale Analysis (64,000+ files)
```bash
# Optimized for large datasets
python run_analysis.py --data-dir modexp/modexp --batch-size 2000

# With transaction enrichment (limited for efficiency)
python run_analysis.py --data-dir modexp/modexp --enrich-txs --max-tx-blocks 5000 --tx-batch-size 250
```

### Standard Analysis
```bash
# Specific number of files
python run_analysis.py --data-dir modexp/modexp --limit 1000 --batch-size 500

# Quick test
python run_analysis.py --quick
```

### Generate Comprehensive Reports
```bash
# Generate enhanced comprehensive analysis report
python generate_enhanced_report.py

# Generate detailed entity-focused analysis with top 50 users
python generate_entity_analysis.py

# Generate basic markdown report from existing data
python generate_markdown_report.py
```

## Performance Optimizations

This analysis is optimized for handling very large datasets:

- **Batched Processing**: Handles 64,000+ files efficiently with configurable batch sizes
- **Memory Management**: Processes data in batches to prevent memory issues
- **Targeted Queries**: Optimized pyxatu queries using transaction hash filtering
- **Compressed Output**: Uses parquet format for large datasets
- **Robust Error Handling**: Continues processing despite individual file failures

## Usage

### Command Line Analysis

```bash
python run_analysis.py [OPTIONS]

Options:
  --data-dir PATH        Directory containing ModExp parquet files (default: modexp/modexp)
  --output-dir PATH      Output directory for results (default: analysis_output)
  --limit N             Limit number of files to process
  --batch-size N        Batch size for file processing (default: 1000)
  --enrich-txs          Enrich with transaction data from Xatu
  --max-tx-blocks N     Max blocks for transaction enrichment (default: 10000)
  --tx-batch-size N     Batch size for transaction queries (default: 500)
  --quick               Quick analysis with limited data (100 files)
```

### Custom Data Directory

To run analysis on a different server with different data location:

```bash
python run_analysis.py --data-dir /path/to/your/modexp/data --output-dir /path/to/output
```

### Programmatic Usage

```python
from eip7883_analysis import ModExpDataAnalyzer

# Initialize with your data directory
analyzer = ModExpDataAnalyzer("/path/to/modexp/data")

# Load and analyze data
df = analyzer.load_modexp_data()
results = analyzer.analyze_impact()

# Generate visualizations
analyzer.create_visualizations("output_directory")
```

## Output Files

The analysis generates several output files:

### Reports
- `eip7883_comprehensive_analysis.md` - Enhanced comprehensive analysis with detailed statistics
- `eip7883_entity_analysis.md` - Entity-focused analysis with top 50 affected addresses (with Etherscan links)
- `analysis_summary.txt` - Summary statistics

### Data Files
- `modexp_analysis_data.parquet` - Complete analysis data in Parquet format
- `top_impacted_senders.csv` - Most affected transaction senders
- `top_impacted_contracts.csv` - Most affected smart contracts
- `entity_projections.csv` - Entity impact projections
- `entity_type_summary.csv` - Summary by entity type

### Interactive Visualizations
- `cost_increase_distribution.html` - Distribution of gas cost increases
- `cost_ratio_by_size.html` - Cost ratios by input parameter sizes
- `cost_timeline.html` - Temporal cost trends
- `sender_impact.html` - Top senders by cost increase
- `contract_impact.html` - Top contracts by cost increase
- `sender_vs_contract_distribution.html` - Comparative impact analysis
- `entity_impact_bubble.html` - Entity impact relationships
- `entity_categories.html` - Entity categorization charts
- `contract_concentration.html` - Contract usage concentration
- `entity_timelines.html` - Entity activity timelines

## Data Format

Input data should be parquet files with the following columns:
- `Bsize`: Base size in bytes
- `Esize`: Exponent size in bytes
- `Msize`: Modulus size in bytes
- `E`: Exponent value (hex string)
- `gas_costs`: Current gas cost
- `tx_hash`: Transaction hash
- `block_number`: Block number (can be derived from filename)

## Key Findings

Based on our comprehensive analysis of 304,301 ModExp calls:

### Impact Overview
- **38.5% of calls affected** by EIP-7883 changes
- **Average increase: 116 gas** per affected call
- **Total additional gas: 35.3M** across all analyzed calls
- **Maximum single increase: 12,805 gas**

### Entity Insights
- **143 unique senders** analyzed, 41 with cost increases
- **Top 10 entities** account for significant portion of impact
- **Power users (top 1%)** represent 30.9% of all calls
- **Most affected address**: 1.8M gas total increase

### Usage Patterns
- **99.975% use standard 32-byte inputs**
- **Fermat prime usage**: 0.4% of calls
- **Network congestion**: Average 0.016% of block gas limit
- **Cost predictability improved**: 42% coefficient of variation (vs 61.7%)

## Dependencies

- pandas
- numpy
- plotly
- pyxatu (optional, for transaction enrichment)
- pathlib
- argparse

## License

MIT