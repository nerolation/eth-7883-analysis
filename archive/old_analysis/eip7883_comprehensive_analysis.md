# EIP-7883 ModExp Comprehensive Analysis Report

*Generated on 2025-07-08 06:54:19*

## Executive Summary

This report provides an in-depth analysis of EIP-7883's impact on ModExp operations based on 304,301 historical Ethereum mainnet calls.

### Key Metrics

**Overall Impact:**
- **Total ModExp calls analyzed**: 304,301
- **Unique transactions**: 75,134
- **Calls with cost increases**: 117,023 (38.5%)
- **Total additional gas required**: 35,308,941 gas
- **Average cost increase**: 116.03 gas per affected call
- **Maximum single call increase**: 12,805 gas

**Economic Impact:**
- **Network congestion**: Average 0.016% of block gas limit
- **Peak congestion**: Maximum 0.360% of block gas limit
- **Cost predictability**: 38.5% of calls affected with 2.50x average increase

## Parameter Analysis

### Input Size Distributions

**Statistical Summary:**
| Parameter | Min | Max | Mean | Median | Std Dev |
|-----------|-----|-----|------|--------|---------|
| Bsize | 32 | 385 | 32.0 | 32 | 2.7 |
| Esize | 1 | 32 | 32.0 | 32 | 0.4 |
| Msize | 32 | 384 | 32.0 | 32 | 2.7 |

**Common Size Combinations:**
| Base Size | Exponent Size | Modulus Size | Count | Percentage |
|-----------|---------------|--------------|-------|------------|
| 32 | 32 | 32 | 304,225 | 100.0% |
| 256 | 3 | 256 | 31 | 0.0% |
| 128 | 1 | 128 | 27 | 0.0% |
| 128 | 32 | 128 | 10 | 0.0% |
| 128 | 3 | 128 | 6 | 0.0% |
| 385 | 3 | 384 | 2 | 0.0% |

### Exponent Analysis

**Fermat Prime Usage**: 1,351 calls (0.4%)

**Most Common Exponent Values:**
| Rank | Exponent | Count | Percentage |
|------|----------|-------|------------|
| 1 | 0x30644e72... | 66,115 | 21.73% |
| 2 | 0xffffffff... | 54,656 | 17.96% |
| 3 | 0x1000000 | 50,599 | 16.63% |
| 4 | 0xffffff | 43,887 | 14.42% |
| 5 | 0xffffffff... | 28,955 | 9.52% |
| 6 | 0xc19139cb... | 20,644 | 6.78% |
| 7 | 0x3fffffff... | 15,463 | 5.08% |
| 8 | 0x1000002 | 6,703 | 2.20% |
| 9 | 0xa59c34 | 6,352 | 2.09% |
| 10 | 0x2000000 | 1,699 | 0.56% |

## Gas Cost Analysis

### Cost Distribution by Impact Category

| Category | Gas Increase Range | Call Count | Percentage | Description |
|----------|-------------------|------------|------------|-------------|
| Minimal | = 150 gas | 0 | 0.0% | Minimum gas increase only |
| Moderate | 151-500 gas | 116974 | 38.4% | Small to moderate impact |
| Significant | 501-1,000 gas | 0 | 0.0% | Notable cost increase |
| Severe | > 1,000 gas | 49 | 0.0% | Major cost impact |

### Gas Efficiency Metrics

**Cost per Byte Analysis:**
- **Current (EIP-2565)**: 9.47 gas/byte average
- **Proposed (EIP-7883)**: 10.68 gas/byte average
- **Efficiency change**: +12.7%

**Cost Predictability:**
- **Current std deviation**: 561.47 gas
- **EIP-7883 std deviation**: 431.47 gas
- **Current coefficient of variation**: 61.7%
- **EIP-7883 coefficient of variation**: 42.0%

### Cost Increase Distribution

**Percentiles (for affected calls only):**
| Percentile | Gas Increase |
|------------|--------------|
| 10th | 300 |
| 25th | 300 |
| 50th (median) | 300 |
| 75th | 300 |
| 90th | 300 |
| 95th | 300 |
| 99th | 300 |

## Temporal Analysis

### Usage Patterns Over Time

**Activity Metrics:**
- **Average calls per block**: 4.75
- **Maximum calls in single block**: 150
- **Usage trend**: decreasing (coefficient: -236.0168)

**Peak Usage Blocks:**
| Rank | Block Number | Call Count |
|------|--------------|------------|
| 1 | 22,496,318 | 150 |
| 2 | 22,496,100 | 144 |
| 3 | 21,758,501 | 120 |
| 4 | 21,758,517 | 112 |
| 5 | 21,921,782 | 105 |

## Entity Analysis

### Most Impacted Senders

| Rank | Address | Total Increase (gas) | Avg Increase | Call Count | Current Cost | New Cost |
|------|---------|---------------------|--------------|------------|--------------|----------|
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
| 11 | [0x94a365ca...](https://etherscan.io/address/0x94a365ca808029af8db18257ecd296c16c61ac05) | 75,600 | 117.21 | 645 | 577,746 | 653,346 |
| 12 | [0xad0a80a0...](https://etherscan.io/address/0xad0a80a085095eca46de3053c345516f1c722d2a) | 64,800 | 209.71 | 309 | 168,657 | 233,457 |
| 13 | [0x52ff08f3...](https://etherscan.io/address/0x52ff08f313a00a54e3beffb5c4a7f7446efb6754) | 57,600 | 150 | 384 | 297,408 | 355,008 |
| 14 | [0x01c3a1a6...](https://etherscan.io/address/0x01c3a1a6890a146ac187a019f9863b3ab2bff91e) | 49,200 | 240 | 205 | 88,109 | 137,309 |
| 15 | [0x2572835e...](https://etherscan.io/address/0x2572835e02b59078711aa0800490e80975e4169d) | 37,800 | 225 | 168 | 81,858 | 119,658 |

### Most Impacted Contracts

| Rank | Contract | Total Increase (gas) | Avg Increase | Calls | Unique Users | Current Cost | New Cost |
|------|----------|---------------------|--------------|-------|--------------|--------------|----------|
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
| 11 | [0x30efaaa9...](https://etherscan.io/address/0x30efaaa99f8efe310d9fdc83072e2a04c093d400) | 14,100 | 300 | 47 | 1 | 9,400 | 23,500 |
| 12 | [0xd1ce9000...](https://etherscan.io/address/0xd1ce90003a10e6dab877890ab1fd96511555e4b3) | 10,920 | 1,365 | 8 | 1 | 10,920 | 21,840 |
| 13 | [0xb4544083...](https://etherscan.io/address/0xb45440830bd8d288bb2b5b01be303ae60fc855d8) | 10,800 | 150 | 72 | 1 | 55,764 | 66,564 |
| 14 | [0xfeda03b9...](https://etherscan.io/address/0xfeda03b91514d31b435d4e1519fd9e699c29bbfc) | 3,300 | 300 | 11 | 4 | 2,200 | 5,500 |
| 15 | [0x2f3c2056...](https://etherscan.io/address/0x2f3c205613d9451f88e19e011ed23775afe00c41) | 2,700 | 150 | 18 | 1 | 13,941 | 16,641 |

### Entity Behavior Patterns

**Power Users Analysis:**
- **Number of power users**: 2
- **Threshold (top 1%)**: ≥7765 calls
- **Total calls by power users**: 17,379
- **Percentage of all calls**: 30.9%

**Multi-Contract Usage:**
- **Users with multiple contracts**: 14
- **Average contracts per user**: 1.10
- **Maximum contracts per user**: 2

## Visualizations

Interactive charts are available in the analysis_output directory:

- **`cost_increase_distribution.html`** - Distribution of gas cost increases
- **`cost_ratio_by_size.html`** - Cost ratios by input parameter sizes  
- **`cost_timeline.html`** - Gas cost trends over time
- **`sender_impact.html`** - Top transaction senders by cost increase
- **`contract_impact.html`** - Top contracts by cost increase
- **`sender_vs_contract_distribution.html`** - Comparative impact distribution

## Technical Details

### EIP-7883 Implementation

The proposal modifies ModExp gas calculation in three key areas:

1. **Multiplication Complexity**: 
   - ≤32 bytes: Fixed cost of 16 (simplified from EIP-2565)
   - >32 bytes: 2 × words² (simplified formula)

2. **Iteration Count Multiplier**: 
   - Increased from 8× to 16× for exponents >32 bytes
   - Addresses underpricing of large exponent operations

3. **Minimum Gas Cost**: 
   - Raised from 200 to 500 gas
   - Prevents abuse of small input operations

### Data Methodology

- **Data source**: Ethereum mainnet ModExp precompile (0x05) calls
- **Block range**: 21,659,928 to 22,785,670 (1,125,743 blocks)
- **Analysis date**: 2025-07-08
- **Total calls analyzed**: 304,301
- **Gas calculations**: Verified against EIP-2565 and EIP-7883 specifications

## Key Findings and Recommendations

### Impact Summary

1. **Concentrated Impact**: 38.5% of calls see cost increases
2. **Predictable Changes**: Most increases follow clear patterns based on input sizes
3. **Security Enhancement**: Addresses DoS vectors while maintaining reasonable costs
4. **Entity Concentration**: Top 10 addresses account for significant portion of impact

### Recommendations by Stakeholder

**For Affected Users:**
- Review ModExp usage patterns and adjust gas limits
- Consider optimizing input sizes where possible
- Budget for average 116 gas increase per call

**For Infrastructure Providers:**
- Update gas estimation algorithms for EIP-7883
- Monitor actual usage post-implementation
- Provide migration guidance for affected users

**For Protocol Developers:**
- Consider targeted outreach to top impacted entities
- Monitor for usage pattern changes post-activation
- Evaluate effectiveness of DoS protection measures

### Conclusion

EIP-7883 represents a targeted security improvement to the ModExp precompile with limited but concentrated impact. The analysis shows that while most operations remain unaffected, specific use cases—particularly those with large exponents or minimal inputs—will see notable cost increases. The predictable nature of these changes allows for effective planning and mitigation by affected parties.

---

*Report generated from historical Ethereum mainnet data. All gas calculations independently verified against EIP specifications.*
