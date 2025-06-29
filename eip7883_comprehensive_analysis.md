# EIP-7883 ModExp Analysis Report

*Generated on 2025-06-29 17:12:04*

## Executive Summary

EIP-7883 impact analysis based on historical Ethereum mainnet data with statistical and entity-level insights.

### Key Findings

- **Total ModExp calls analyzed**: 304,301
- **Unique transactions**: 75,134
- **Calls with cost increases**: 117,023 (38.5% of all calls)
- **Total additional gas required**: 35,308,941 gas
- **Average cost increase per affected call**: 116.03 gas
- **Maximum single call increase**: 12,805 gas

## Entity Analysis

### Most Impacted Senders

Addresses with highest total gas cost increases:

| Rank | Address | Total Increase (gas) | Avg Increase | Call Count | Current Total Cost | New Total Cost |
|------|---------|---------------------|--------------|------------|-------------------|----------------|
| 1 | [0xaaf7b278...](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | 1,797,600 | 224.67 | 8,001 | 3,908,541 | 5,706,141 |
| 2 | [0x54ab716d...](https://etherscan.io/address/0x54ab716d465be3d5eeca64e63ac0048d7a81659a) | 1,661,400 | 223.31 | 7,440 | 3,673,398 | 5,334,798 |
| 3 | [0x00000062...](https://etherscan.io/address/0x000000629fbcf27a347d1aeba658435230d74a5f) | 1,406,700 | 150 | 9,378 | 7,263,261 | 8,669,961 |
| 4 | [0xf3b07f67...](https://etherscan.io/address/0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f) | 745,800 | 223.43 | 3,338 | 1,646,548 | 2,392,348 |
| 5 | [0xfcb73f64...](https://etherscan.io/address/0xfcb73f6405f6b9be91013d9477d81833a69c9c0d) | 621,900 | 150 | 4,146 | 3,211,077 | 3,832,977 |
| 6 | [0x58d14960...](https://etherscan.io/address/0x58d14960e0a2be353edde61ad719196a2b816522) | 345,600 | 219.99 | 1,571 | 795,631 | 1,141,231 |
| 7 | [0x2b711ee0...](https://etherscan.io/address/0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d) | 248,400 | 225 | 1,104 | 537,924 | 786,324 |
| 8 | [0x35274399...](https://etherscan.io/address/0x3527439923a63f8c13cf72b8fe80a77f6e572092) | 243,600 | 218.87 | 1,113 | 568,449 | 812,049 |
| 9 | [0xc2adcfcc...](https://etherscan.io/address/0xc2adcfccee33a417064d1a45d3b202de6d9fa474) | 123,300 | 150 | 822 | 636,639 | 759,939 |
| 10 | [0x9c0b0dbb...](https://etherscan.io/address/0x9c0b0dbbae8a976ceea8c2a96f6d00c53839afdc) | 112,500 | 150 | 750 | 580,875 | 693,375 |

### Most Impacted Contracts

Contracts with highest total gas cost increases:

| Rank | Contract Address | Total Increase (gas) | Avg Increase | Call Count | Unique Users | Current Total Cost | New Total Cost |
|------|------------------|---------------------|--------------|------------|--------------|-------------------|----------------|
| 1 | [0x8c0bfc04...](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) | 2,993,400 | 218.56 | 13,696 | 17 | 7,011,182 | 10,004,582 |
| 2 | [0x5d8ba173...](https://etherscan.io/address/0x5d8ba173dc6c3c90c8f7c04c9288bef5fdbad06e) | 2,286,000 | 225 | 10,160 | 9 | 4,950,460 | 7,236,460 |
| 3 | [0x68d30f47...](https://etherscan.io/address/0x68d30f47f19c07bccef4ac7fae2dc12fca3e0dc9) | 1,406,700 | 150 | 9,378 | 1 | 7,263,261 | 8,669,961 |
| 4 | [0x3b4d794a...](https://etherscan.io/address/0x3b4d794a66304f130a4db8f2551b0070dfcf5ca7) | 621,900 | 150 | 4,146 | 1 | 3,211,077 | 3,832,977 |
| 5 | [0x02993cdc...](https://etherscan.io/address/0x02993cdc11213985b9b13224f3af289f03bf298d) | 123,300 | 150 | 822 | 1 | 636,639 | 759,939 |
| 6 | [0x7cf3876f...](https://etherscan.io/address/0x7cf3876f681dbb6eda8f6ffc45d66b996df08fae) | 112,500 | 150 | 750 | 1 | 580,875 | 693,375 |
| 7 | [0xece9cf6a...](https://etherscan.io/address/0xece9cf6a8f2768a3b8b65060925b646afeaa5167) | 75,600 | 117.21 | 645 | 1 | 577,746 | 653,346 |
| 8 | [0xd19d4b5d...](https://etherscan.io/address/0xd19d4b5d358258f05d7b411e21a1460d11b0876f) | 57,600 | 150 | 384 | 1 | 297,408 | 355,008 |
| 9 | [0xabea9132...](https://etherscan.io/address/0xabea9132b05a70803a4e85094fd0e1800777fbef) | 49,200 | 240 | 205 | 1 | 88,109 | 137,309 |
| 10 | [0xb32cb567...](https://etherscan.io/address/0xb32cb5677a7c971689228ec835800432b339ba2b) | 35,496 | 4,437 | 8 | 2 | 35,496 | 70,992 |

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

### Data Scope
- **Block range**: 21,659,928 to 22,785,670 (1,125,743 blocks)
- **Total calls analyzed**: 304,301
- **Data source**: Ethereum mainnet ModExp precompile calls
- **Analysis date**: 2025-06-29

### Methods
- Gas costs calculated using EIP-2565 and EIP-7883 formulas
- Increases represent additional gas required under EIP-7883
- Entity analysis groups by senders and contracts
- Percentiles exclude zero-increase calls

## Conclusions and Implications

### Impact Assessment

1. **Limited scope**: Only 38.5% of calls affected
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

Analysis based on historical mainnet data (304,301 calls). ModExp precompile primarily used by cryptographic applications and ZK proof systems.

---

*Report generated using historical Ethereum mainnet data. Gas calculations verified against EIP-2565 and EIP-7883 specifications.*
