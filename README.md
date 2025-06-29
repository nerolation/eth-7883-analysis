# EIP-7883 ModExp Gas Cost Analysis

Empirical analysis of the impact of EIP-7883 on Ethereum's ModExp precompile gas costs.

## Overview

EIP-7883 proposes changes to the ModExp precompile pricing to address underpricing in certain edge cases. This analysis examines historical ModExp usage to quantify the impact of these changes.

### Key Changes in EIP-7883:
- Minimum gas cost increased from 200 to 500
- Exponent length cost multiplier increased from 8 to 16
- Modified multiplication complexity calculation

## Quick Start

### Basic Analysis
```bash
python run_analysis.py --data-dir modexp/modexp --output-dir analysis_output
```

### Full Analysis with Transaction Data
```bash
python run_analysis.py --data-dir modexp/modexp --output-dir analysis_output --enrich-txs
```

### Interactive Analysis
```bash
jupyter notebook eip7883_interactive_analysis.ipynb
```

## Usage

### Command Line Analysis

The main analysis script supports several options:

```bash
python run_analysis.py [OPTIONS]

Options:
  --data-dir PATH      Directory containing ModExp parquet files (default: modexp/modexp)
  --output-dir PATH    Output directory for results (default: analysis_output)
  --limit N           Limit number of files to process
  --enrich-txs        Enrich with transaction data from Xatu
  --quick             Quick analysis with limited data (100 files)
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

- `eip7883_analysis_report.md` - Comprehensive analysis report
- `summary_statistics.csv` - Key statistics in CSV format
- `affected_protocols.csv` - Protocols most impacted (if tx data available)
- `cost_increase_distribution.html` - Interactive visualization of cost increases
- `cost_ratio_by_size.html` - Cost ratios by input size
- `cost_timeline.html` - Cost changes over time
- `address_impact.html` - Impact by address (if tx data available)

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

Based on the analysis:
- Only calls with large inputs (>32 bytes) see significant cost increases
- The minimum cost increase from 200 to 500 gas affects small operations
- Average cost increase varies by usage pattern
- Most common use cases see minimal impact

## Dependencies

- pandas
- numpy
- plotly
- pyxatu (optional, for transaction enrichment)
- pathlib
- argparse

## License

MIT