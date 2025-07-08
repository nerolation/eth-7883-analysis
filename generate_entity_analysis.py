#!/usr/bin/env python3
"""
Sophisticated entity-focused analysis for EIP-7883 ModExp impact
Generates detailed tables with 50 most affected users and contracts
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def load_data(analysis_dir: Path):
    """Load all necessary data files"""
    parquet_path = analysis_dir / "modexp_analysis_data.parquet"
    if parquet_path.exists():
        df = pd.read_parquet(parquet_path)
    else:
        raise FileNotFoundError(f"Parquet file not found at {parquet_path}")
    
    return df


def format_address_with_link(address: str, full: bool = False) -> str:
    """Format address with Etherscan link"""
    if pd.isna(address) or address == '':
        return 'N/A'
    
    if full:
        return f"[{address}](https://etherscan.io/address/{address})"
    else:
        return f"[{address[:6]}...{address[-4:]}](https://etherscan.io/address/{address})"


def format_number(num):
    """Format numbers with commas"""
    if isinstance(num, (int, float)):
        if abs(num) >= 1_000_000:
            return f"{num/1_000_000:,.2f}M"
        elif abs(num) >= 1_000:
            return f"{num/1_000:,.1f}K" if num == int(num/1_000)*1_000 else f"{num:,.0f}"
        else:
            return f"{num:,.0f}" if num == int(num) else f"{num:,.2f}"
    return str(num)


def analyze_entity_categories(df: pd.DataFrame) -> dict:
    """Categorize entities based on their behavior patterns"""
    # Focus on entities with sender information
    sender_df = df[df['from_address'].notna()].copy()
    
    # Calculate entity metrics
    entity_metrics = sender_df.groupby('from_address').agg({
        'cost_increase': ['sum', 'mean', 'count'],
        'eip2565_cost': 'sum',
        'eip7883_cost': 'sum',
        'block_number': ['min', 'max', 'nunique'],
        'tx_hash': 'nunique',
        'to_address': lambda x: x.nunique() if 'to_address' in sender_df.columns else 0
    })
    
    # Flatten column names
    entity_metrics.columns = ['_'.join(col).strip() for col in entity_metrics.columns.values]
    entity_metrics = entity_metrics.rename(columns={
        'cost_increase_sum': 'total_increase',
        'cost_increase_mean': 'avg_increase',
        'cost_increase_count': 'call_count',
        'eip2565_cost_sum': 'total_current_cost',
        'eip7883_cost_sum': 'total_new_cost',
        'block_number_min': 'first_block',
        'block_number_max': 'last_block',
        'block_number_nunique': 'active_blocks',
        'tx_hash_nunique': 'unique_txs',
        'to_address_<lambda>': 'unique_contracts'
    })
    
    # Calculate derived metrics
    entity_metrics['pct_increase'] = (entity_metrics['total_increase'] / entity_metrics['total_current_cost'] * 100).fillna(0)
    entity_metrics['activity_span'] = entity_metrics['last_block'] - entity_metrics['first_block']
    entity_metrics['calls_per_1000_blocks'] = (entity_metrics['call_count'] / (entity_metrics['activity_span'] / 1000)).replace([np.inf, -np.inf], 0).fillna(0)
    entity_metrics['avg_calls_per_tx'] = entity_metrics['call_count'] / entity_metrics['unique_txs']
    
    # Categorize entities
    categories = []
    for idx, row in entity_metrics.iterrows():
        if row['call_count'] >= 5000:
            category = 'Heavy User'
        elif row['call_count'] >= 1000:
            category = 'Frequent User'
        elif row['call_count'] >= 100:
            category = 'Regular User'
        elif row['call_count'] >= 10:
            category = 'Occasional User'
        else:
            category = 'Rare User'
        
        # Sub-categorize by impact
        if row['total_increase'] >= 100_000:
            category += ' - High Impact'
        elif row['total_increase'] >= 10_000:
            category += ' - Medium Impact'
        else:
            category += ' - Low Impact'
        
        categories.append(category)
    
    entity_metrics['category'] = categories
    
    return entity_metrics


def analyze_contract_usage(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze contract usage patterns"""
    if 'to_address' not in df.columns:
        return pd.DataFrame()
    
    contract_df = df[df['to_address'].notna()].copy()
    
    contract_metrics = contract_df.groupby('to_address').agg({
        'cost_increase': ['sum', 'mean', 'count'],
        'eip2565_cost': 'sum',
        'eip7883_cost': 'sum',
        'from_address': lambda x: x.nunique() if x.notna().any() else 0,
        'block_number': ['min', 'max', 'nunique'],
        'tx_hash': 'nunique'
    })
    
    # Flatten column names
    contract_metrics.columns = ['_'.join(col).strip() for col in contract_metrics.columns.values]
    contract_metrics = contract_metrics.rename(columns={
        'cost_increase_sum': 'total_increase',
        'cost_increase_mean': 'avg_increase',
        'cost_increase_count': 'call_count',
        'eip2565_cost_sum': 'total_current_cost',
        'eip7883_cost_sum': 'total_new_cost',
        'from_address_<lambda>': 'unique_users',
        'block_number_min': 'first_block',
        'block_number_max': 'last_block',
        'block_number_nunique': 'active_blocks',
        'tx_hash_nunique': 'unique_txs'
    })
    
    # Calculate derived metrics
    contract_metrics['pct_increase'] = (contract_metrics['total_increase'] / contract_metrics['total_current_cost'] * 100).fillna(0)
    contract_metrics['avg_calls_per_user'] = contract_metrics['call_count'] / contract_metrics['unique_users'].replace(0, 1)
    contract_metrics['concentration_score'] = 1 - (contract_metrics['unique_users'] / contract_metrics['call_count']).clip(0, 1)
    
    return contract_metrics


def create_entity_visualizations(entity_metrics: pd.DataFrame, contract_metrics: pd.DataFrame, output_dir: Path):
    """Create sophisticated entity-focused visualizations"""
    
    # 1. Entity Impact Bubble Chart
    top_entities = entity_metrics.nlargest(30, 'total_increase')
    
    fig = px.scatter(top_entities.reset_index(), 
                     x='call_count', 
                     y='avg_increase',
                     size='total_increase',
                     color='pct_increase',
                     hover_data=['from_address', 'total_increase', 'unique_contracts'],
                     title='Entity Impact Analysis: Call Volume vs Average Increase',
                     labels={'call_count': 'Total Calls', 
                            'avg_increase': 'Average Gas Increase per Call',
                            'pct_increase': '% Increase'},
                     color_continuous_scale='Reds')
    
    fig.update_layout(height=600, width=1000)
    fig.write_html(output_dir / 'entity_impact_bubble.html')
    
    # 2. Entity Category Distribution
    category_stats = entity_metrics.reset_index().groupby('category').agg({
        'total_increase': 'sum',
        'call_count': 'sum',
        'from_address': 'count'
    }).rename(columns={'from_address': 'entity_count'})
    
    fig = make_subplots(rows=1, cols=2, 
                        subplot_titles=('Total Gas Increase by Category', 'Entity Count by Category'),
                        specs=[[{'type': 'pie'}, {'type': 'pie'}]])
    
    fig.add_trace(go.Pie(labels=category_stats.index, 
                         values=category_stats['total_increase'],
                         name='Gas Increase'),
                  row=1, col=1)
    
    fig.add_trace(go.Pie(labels=category_stats.index, 
                         values=category_stats['entity_count'],
                         name='Entity Count'),
                  row=1, col=2)
    
    fig.update_layout(height=500, width=1200, title_text='Entity Category Analysis')
    fig.write_html(output_dir / 'entity_categories.html')
    
    # 3. Contract Concentration Analysis
    if not contract_metrics.empty:
        top_contracts = contract_metrics.nlargest(20, 'total_increase')
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=top_contracts.index,
            y=top_contracts['call_count'],
            name='Total Calls',
            yaxis='y',
            marker_color='lightblue'
        ))
        
        fig.add_trace(go.Scatter(
            x=top_contracts.index,
            y=top_contracts['unique_users'],
            name='Unique Users',
            yaxis='y2',
            mode='lines+markers',
            marker_color='red'
        ))
        
        fig.update_layout(
            title='Contract Usage Concentration: Calls vs Unique Users',
            xaxis_title='Contract Address',
            yaxis=dict(title='Total Calls', side='left'),
            yaxis2=dict(title='Unique Users', overlaying='y', side='right'),
            height=600,
            width=1200
        )
        
        fig.write_html(output_dir / 'contract_concentration.html')
    
    # 4. Entity Activity Timeline
    top_active = entity_metrics.nlargest(10, 'call_count')
    
    fig = go.Figure()
    
    for i, (addr, row) in enumerate(top_active.iterrows()):
        fig.add_trace(go.Scatter(
            x=[row['first_block'], row['last_block']],
            y=[i, i],
            mode='lines+markers',
            name=f"{addr[:6]}...{addr[-4:]}",
            line=dict(width=10),
            marker=dict(size=15)
        ))
    
    fig.update_layout(
        title='Entity Activity Timelines (Top 10 by Call Count)',
        xaxis_title='Block Number',
        yaxis_title='Entity',
        height=600,
        width=1000,
        showlegend=True
    )
    
    fig.write_html(output_dir / 'entity_timelines.html')


def generate_entity_report(analysis_dir: Path, output_file: str):
    """Generate comprehensive entity-focused analysis report"""
    
    # Load data
    df = load_data(analysis_dir)
    
    # Perform entity analysis
    entity_metrics = analyze_entity_categories(df)
    contract_metrics = analyze_contract_usage(df)
    
    # Sort entities by total increase
    top_entities = entity_metrics.nlargest(50, 'total_increase')
    top_contracts = contract_metrics.nlargest(50, 'total_increase') if not contract_metrics.empty else pd.DataFrame()
    
    # Create visualizations
    create_entity_visualizations(entity_metrics, contract_metrics, analysis_dir)
    
    # Generate report
    report = f"""# EIP-7883 Entity Impact Analysis

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Executive Summary

This report provides detailed entity-level analysis of EIP-7883's impact, focusing on the most affected addresses and their usage patterns.

### Key Statistics

- **Total unique senders analyzed**: {format_number(entity_metrics.index.nunique())}
- **Senders with cost increases**: {format_number((entity_metrics['total_increase'] > 0).sum())}
- **Total unique contracts**: {format_number(contract_metrics.index.nunique() if not contract_metrics.empty else 0)}
- **Contracts with increased costs**: {format_number((contract_metrics['total_increase'] > 0).sum() if not contract_metrics.empty else 0)}

### Entity Categories

| Category | Entity Count | Total Gas Increase | Total Calls | Avg Increase per Entity |
|----------|--------------|-------------------|-------------|-------------------------|"""

    # Add category statistics
    category_summary = entity_metrics.reset_index().groupby('category').agg({
        'total_increase': ['sum', 'mean'],
        'call_count': 'sum',
        'from_address': 'count'
    })
    
    for cat in sorted(category_summary.index):
        stats = category_summary.loc[cat]
        report += f"\n| {cat} | {format_number(stats[('from_address', 'count')])} | {format_number(stats[('total_increase', 'sum')])} | {format_number(stats[('call_count', 'sum')])} | {format_number(stats[('total_increase', 'mean')])} |"

    report += """

## Top 50 Most Affected Entities

### By Total Gas Increase

| Rank | Address | Category | Total Increase | Avg per Call | Total Calls | Unique Contracts | % Increase | Current Cost | New Cost |
|------|---------|----------|----------------|--------------|-------------|------------------|------------|--------------|----------|"""

    # Add top 50 entities
    for i, (addr, row) in enumerate(top_entities.iterrows(), 1):
        report += f"""
| {i} | {format_address_with_link(addr, full=True)} | {row['category']} | {format_number(row['total_increase'])} | {format_number(row['avg_increase'])} | {format_number(row['call_count'])} | {row['unique_contracts']} | {row['pct_increase']:.1f}% | {format_number(row['total_current_cost'])} | {format_number(row['total_new_cost'])} |"""

    # Add activity patterns section
    report += """

## Entity Activity Patterns

### Most Active Entities

| Rank | Address | Total Calls | Active Blocks | Calls/1K Blocks | First Block | Last Block | Activity Span |
|------|---------|-------------|---------------|-----------------|-------------|------------|---------------|"""

    most_active = entity_metrics.nlargest(20, 'call_count')
    for i, (addr, row) in enumerate(most_active.iterrows(), 1):
        report += f"""
| {i} | {format_address_with_link(addr)} | {format_number(row['call_count'])} | {format_number(row['active_blocks'])} | {row['calls_per_1000_blocks']:.1f} | {format_number(row['first_block'])} | {format_number(row['last_block'])} | {format_number(row['activity_span'])} blocks |"""

    # Add highest impact per call section
    report += """

### Highest Average Impact per Call

| Rank | Address | Avg Increase/Call | Total Calls | Total Increase | Category |
|------|---------|-------------------|-------------|----------------|----------|"""

    high_avg_impact = entity_metrics[entity_metrics['call_count'] >= 10].nlargest(20, 'avg_increase')
    for i, (addr, row) in enumerate(high_avg_impact.iterrows(), 1):
        report += f"""
| {i} | {format_address_with_link(addr)} | {format_number(row['avg_increase'])} | {format_number(row['call_count'])} | {format_number(row['total_increase'])} | {row['category']} |"""

    # Contract analysis section
    if not contract_metrics.empty:
        report += """

## Top 50 Most Affected Contracts

| Rank | Contract Address | Total Increase | Avg per Call | Total Calls | Unique Users | User Concentration | % Increase | Current Cost | New Cost |
|------|------------------|----------------|--------------|-------------|--------------|-------------------|------------|--------------|----------|"""

        for i, (addr, row) in enumerate(top_contracts.iterrows(), 1):
            report += f"""
| {i} | {format_address_with_link(addr, full=True)} | {format_number(row['total_increase'])} | {format_number(row['avg_increase'])} | {format_number(row['call_count'])} | {format_number(row['unique_users'])} | {row['concentration_score']:.2f} | {row['pct_increase']:.1f}% | {format_number(row['total_current_cost'])} | {format_number(row['total_new_cost'])} |"""

        # Most used contracts
        report += """

### Most Used Contracts by Unique Users

| Rank | Contract Address | Unique Users | Total Calls | Avg Calls/User | Total Increase |
|------|------------------|--------------|-------------|----------------|----------------|"""

        most_used = contract_metrics.nlargest(20, 'unique_users')
        for i, (addr, row) in enumerate(most_used.iterrows(), 1):
            report += f"""
| {i} | {format_address_with_link(addr)} | {format_number(row['unique_users'])} | {format_number(row['call_count'])} | {row['avg_calls_per_user']:.1f} | {format_number(row['total_increase'])} |"""

    # Entity relationships
    report += """

## Entity Relationships

### Multi-Contract Users

Entities using multiple contracts (top 20 by total impact):

| Rank | Entity Address | Contracts Used | Total Calls | Total Increase | Primary Contract |
|------|----------------|----------------|-------------|----------------|------------------|"""

    multi_contract_users = entity_metrics[entity_metrics['unique_contracts'] > 1].nlargest(20, 'total_increase')
    
    for i, (addr, row) in enumerate(multi_contract_users.iterrows(), 1):
        # Find primary contract for this user
        user_contracts = df[(df['from_address'] == addr) & df['to_address'].notna()]['to_address'].value_counts()
        primary_contract = user_contracts.index[0] if len(user_contracts) > 0 else 'N/A'
        
        report += f"""
| {i} | {format_address_with_link(addr)} | {row['unique_contracts']} | {format_number(row['call_count'])} | {format_number(row['total_increase'])} | {format_address_with_link(primary_contract)} |"""

    # Power user analysis
    power_threshold = entity_metrics['call_count'].quantile(0.99)
    power_users = entity_metrics[entity_metrics['call_count'] >= power_threshold]
    
    report += f"""

## Power User Analysis

Entities in the top 1% by call volume (≥{format_number(power_threshold)} calls):

| Rank | Address | Total Calls | Total Increase | % of All Calls | % of All Increase | Category |
|------|---------|-------------|----------------|----------------|-------------------|----------|"""

    total_calls = entity_metrics['call_count'].sum()
    total_increase = entity_metrics['total_increase'].sum()
    
    for i, (addr, row) in enumerate(power_users.nlargest(20, 'call_count').iterrows(), 1):
        pct_calls = row['call_count'] / total_calls * 100
        pct_increase = row['total_increase'] / total_increase * 100 if total_increase > 0 else 0
        
        report += f"""
| {i} | {format_address_with_link(addr)} | {format_number(row['call_count'])} | {format_number(row['total_increase'])} | {pct_calls:.2f}% | {pct_increase:.2f}% | {row['category']} |"""

    # Summary statistics
    report += f"""

## Summary Statistics

### Entity Distribution

- **Heavy Users (≥5,000 calls)**: {(entity_metrics['call_count'] >= 5000).sum()} entities
- **Frequent Users (1,000-4,999 calls)**: {((entity_metrics['call_count'] >= 1000) & (entity_metrics['call_count'] < 5000)).sum()} entities
- **Regular Users (100-999 calls)**: {((entity_metrics['call_count'] >= 100) & (entity_metrics['call_count'] < 1000)).sum()} entities
- **Occasional Users (10-99 calls)**: {((entity_metrics['call_count'] >= 10) & (entity_metrics['call_count'] < 100)).sum()} entities
- **Rare Users (<10 calls)**: {(entity_metrics['call_count'] < 10).sum()} entities

### Impact Distribution

- **High Impact (≥100K gas increase)**: {(entity_metrics['total_increase'] >= 100_000).sum()} entities
- **Medium Impact (10K-99K gas)**: {((entity_metrics['total_increase'] >= 10_000) & (entity_metrics['total_increase'] < 100_000)).sum()} entities
- **Low Impact (<10K gas)**: {(entity_metrics['total_increase'] < 10_000).sum()} entities

### Concentration Metrics

- **Top 10 entities**: {entity_metrics.nlargest(10, 'total_increase')['total_increase'].sum() / total_increase * 100:.1f}% of total gas increase
- **Top 50 entities**: {entity_metrics.nlargest(50, 'total_increase')['total_increase'].sum() / total_increase * 100:.1f}% of total gas increase
- **Top 100 entities**: {entity_metrics.nlargest(100, 'total_increase')['total_increase'].sum() / total_increase * 100:.1f}% of total gas increase

## Interactive Visualizations

The following interactive charts have been generated:

- **`entity_impact_bubble.html`** - Bubble chart showing entity impact relationships
- **`entity_categories.html`** - Distribution of entities by category and impact
- **`contract_concentration.html`** - Contract usage concentration analysis
- **`entity_timelines.html`** - Activity timelines for top entities

## Methodology

- **Data source**: Ethereum mainnet ModExp precompile calls
- **Entity identification**: Based on transaction 'from' addresses
- **Impact calculation**: Sum of all gas cost increases under EIP-7883
- **Categorization**: Based on usage patterns and impact levels
- **Concentration score**: Measures how concentrated contract usage is (0=distributed, 1=single user)

---

*This entity-focused analysis provides detailed insights into how EIP-7883 impacts different users of the ModExp precompile.*
"""

    # Write report
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"Entity analysis report saved to {output_file}")


def main():
    """Main execution function"""
    analysis_dir = Path("analysis_output")
    
    if not analysis_dir.exists():
        print(f"ERROR: Analysis directory {analysis_dir} does not exist")
        return
    
    print("Generating entity-focused analysis report...")
    generate_entity_report(analysis_dir, "eip7883_entity_analysis.md")


if __name__ == "__main__":
    main()