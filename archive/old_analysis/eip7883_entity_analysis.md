# EIP-7883 Entity Impact Analysis

*Generated on 2025-07-08 07:06:12*

## Executive Summary

This report provides detailed entity-level analysis of EIP-7883's impact, focusing on the most affected addresses and their usage patterns.

### Key Statistics

- **Total unique senders analyzed**: 143
- **Senders with cost increases**: 41
- **Total unique contracts**: 42
- **Contracts with increased costs**: 18

### Entity Categories

| Category | Entity Count | Total Gas Increase | Total Calls | Avg Increase per Entity |
|----------|--------------|-------------------|-------------|-------------------------|
| Frequent User - High Impact | 5 | 2.21M | 11,272 | 441,060 |
| Frequent User - Low Impact | 3 | 0 | 6,763 | 0 |
| Heavy User - High Impact | 3 | 4.87M | 24,819 | 1.62M |
| Occasional User - Low Impact | 64 | 21,900 | 3,150 | 342.19 |
| Occasional User - Medium Impact | 2 | 24,900 | 119 | 12,450 |
| Rare User - Low Impact | 36 | 6,600 | 113 | 183.33 |
| Rare User - Medium Impact | 3 | 46,416 | 16 | 15,472 |
| Regular User - High Impact | 2 | 235,800 | 1,572 | 117,900 |
| Regular User - Low Impact | 15 | 0 | 6,069 | 0 |
| Regular User - Medium Impact | 10 | 400,200 | 2,426 | 40,020 |

## Top 50 Most Affected Entities

### By Total Gas Increase

| Rank | Address | Category | Total Increase | Avg per Call | Total Calls | Unique Contracts | % Increase | Current Cost | New Cost |
|------|---------|----------|----------------|--------------|-------------|------------------|------------|--------------|----------|
| 1 | [0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | Heavy User - High Impact | 1.80M | 224.67 | 8,001 | 2 | 46.0% | 3.91M | 5.71M |
| 2 | [0x54ab716d465be3d5eeca64e63ac0048d7a81659a](https://etherscan.io/address/0x54ab716d465be3d5eeca64e63ac0048d7a81659a) | Heavy User - High Impact | 1.66M | 223.31 | 7,440 | 2 | 45.2% | 3.67M | 5.33M |
| 3 | [0x000000629fbcf27a347d1aeba658435230d74a5f](https://etherscan.io/address/0x000000629fbcf27a347d1aeba658435230d74a5f) | Heavy User - High Impact | 1.41M | 150 | 9,378 | 1 | 19.4% | 7.26M | 8.67M |
| 4 | [0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f](https://etherscan.io/address/0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f) | Frequent User - High Impact | 745,800 | 223.43 | 3,338 | 2 | 45.3% | 1.65M | 2.39M |
| 5 | [0xfcb73f6405f6b9be91013d9477d81833a69c9c0d](https://etherscan.io/address/0xfcb73f6405f6b9be91013d9477d81833a69c9c0d) | Frequent User - High Impact | 621,900 | 150 | 4,146 | 1 | 19.4% | 3.21M | 3.83M |
| 6 | [0x58d14960e0a2be353edde61ad719196a2b816522](https://etherscan.io/address/0x58d14960e0a2be353edde61ad719196a2b816522) | Frequent User - High Impact | 345,600 | 219.99 | 1,571 | 2 | 43.4% | 795,631 | 1.14M |
| 7 | [0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d](https://etherscan.io/address/0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d) | Frequent User - High Impact | 248,400 | 225 | 1,104 | 2 | 46.2% | 537,924 | 786,324 |
| 8 | [0x3527439923a63f8c13cf72b8fe80a77f6e572092](https://etherscan.io/address/0x3527439923a63f8c13cf72b8fe80a77f6e572092) | Frequent User - High Impact | 243,600 | 218.87 | 1,113 | 1 | 42.9% | 568,449 | 812,049 |
| 9 | [0xc2adcfccee33a417064d1a45d3b202de6d9fa474](https://etherscan.io/address/0xc2adcfccee33a417064d1a45d3b202de6d9fa474) | Regular User - High Impact | 123,300 | 150 | 822 | 1 | 19.4% | 636,639 | 759,939 |
| 10 | [0x9c0b0dbbae8a976ceea8c2a96f6d00c53839afdc](https://etherscan.io/address/0x9c0b0dbbae8a976ceea8c2a96f6d00c53839afdc) | Regular User - High Impact | 112,500 | 150 | 750 | 1 | 19.4% | 580,875 | 693,375 |
| 11 | [0x94a365ca808029af8db18257ecd296c16c61ac05](https://etherscan.io/address/0x94a365ca808029af8db18257ecd296c16c61ac05) | Regular User - Medium Impact | 75,600 | 117.21 | 645 | 1 | 13.1% | 577,746 | 653,346 |
| 12 | [0xad0a80a085095eca46de3053c345516f1c722d2a](https://etherscan.io/address/0xad0a80a085095eca46de3053c345516f1c722d2a) | Regular User - Medium Impact | 64,800 | 209.71 | 309 | 1 | 38.4% | 168,657 | 233,457 |
| 13 | [0x52ff08f313a00a54e3beffb5c4a7f7446efb6754](https://etherscan.io/address/0x52ff08f313a00a54e3beffb5c4a7f7446efb6754) | Regular User - Medium Impact | 57,600 | 150 | 384 | 1 | 19.4% | 297,408 | 355,008 |
| 14 | [0x01c3a1a6890a146ac187a019f9863b3ab2bff91e](https://etherscan.io/address/0x01c3a1a6890a146ac187a019f9863b3ab2bff91e) | Regular User - Medium Impact | 49,200 | 240 | 205 | 1 | 55.8% | 88,109 | 137,309 |
| 15 | [0x2572835e02b59078711aa0800490e80975e4169d](https://etherscan.io/address/0x2572835e02b59078711aa0800490e80975e4169d) | Regular User - Medium Impact | 37,800 | 225 | 168 | 2 | 46.2% | 81,858 | 119,658 |
| 16 | [0x59b84b24e307682df830b32ddc826fbbe003c210](https://etherscan.io/address/0x59b84b24e307682df830b32ddc826fbbe003c210) | Regular User - Medium Impact | 32,400 | 225 | 144 | 2 | 46.2% | 70,164 | 102,564 |
| 17 | [0x0f9b807d5b0ce12450059b425dc35c727d65cb2f](https://etherscan.io/address/0x0f9b807d5b0ce12450059b425dc35c727d65cb2f) | Regular User - Medium Impact | 30,600 | 225 | 136 | 2 | 46.2% | 66,266 | 96,866 |
| 18 | [0x415ed64d42bc0c37aeaaef79aa767d963ef38807](https://etherscan.io/address/0x415ed64d42bc0c37aeaaef79aa767d963ef38807) | Regular User - Medium Impact | 21.0K | 120 | 175 | 1 | 13.5% | 155,645 | 176,645 |
| 19 | [0x63023d171098efbc9e7805fa85310b7078902912](https://etherscan.io/address/0x63023d171098efbc9e7805fa85310b7078902912) | Rare User - Medium Impact | 17,748 | 4,437 | 4 | 1 | 413.2% | 4,295 | 35,496 |
| 20 | [0xe51d0862078098c84346b6203b50b996f7dafe28](https://etherscan.io/address/0xe51d0862078098c84346b6203b50b996f7dafe28) | Rare User - Medium Impact | 17,748 | 4,437 | 4 | 1 | 413.2% | 4,295 | 35,496 |
| 21 | [0xcd0b5a01abe9c14f6efbc610c02ecf0fb69855da](https://etherscan.io/address/0xcd0b5a01abe9c14f6efbc610c02ecf0fb69855da) | Regular User - Medium Impact | 17,400 | 120 | 145 | 1 | 13.5% | 128,963 | 146,363 |
| 22 | [0xfe325f97146124f3767bfa59899fa4177fd46d2f](https://etherscan.io/address/0xfe325f97146124f3767bfa59899fa4177fd46d2f) | Occasional User - Medium Impact | 14,100 | 300 | 47 | 1 | 150.0% | 9,400 | 23,500 |
| 23 | [0x30066439887c0a509cb38e45c9262e6924a29bbd](https://etherscan.io/address/0x30066439887c0a509cb38e45c9262e6924a29bbd) | Regular User - Medium Impact | 13,800 | 120 | 115 | 1 | 13.5% | 102,281 | 116,081 |
| 24 | [0xa42033c2314371c0453cec71b9d0628d7ebad887](https://etherscan.io/address/0xa42033c2314371c0453cec71b9d0628d7ebad887) | Rare User - Medium Impact | 10,920 | 1,365 | 8 | 1 | 682.5% | 1,600 | 21,840 |
| 25 | [0xf579a1cdfb89d0aaf240d489ef10ab01a2b7f8f2](https://etherscan.io/address/0xf579a1cdfb89d0aaf240d489ef10ab01a2b7f8f2) | Occasional User - Medium Impact | 10,800 | 150 | 72 | 1 | 19.4% | 55,764 | 66,564 |
| 26 | [0x7fea26a181a792b5107ee0a31e434f5dbcbbe0b7](https://etherscan.io/address/0x7fea26a181a792b5107ee0a31e434f5dbcbbe0b7) | Occasional User - Low Impact | 7,200 | 225 | 32 | 1 | 46.2% | 15,592 | 22,792 |
| 27 | [0xb66d4af4e96bf96026454a6a150edd2ce55e9e67](https://etherscan.io/address/0xb66d4af4e96bf96026454a6a150edd2ce55e9e67) | Occasional User - Low Impact | 3,600 | 225 | 16 | 1 | 46.2% | 7,796 | 11,396 |
| 28 | [0xb9d48daf26f3cbe01a959f09f98e8a2ec8204122](https://etherscan.io/address/0xb9d48daf26f3cbe01a959f09f98e8a2ec8204122) | Occasional User - Low Impact | 3,600 | 225 | 16 | 1 | 46.2% | 7,796 | 11,396 |
| 29 | [0x477c1b7dc1091389cbd3eef21efb00081606ab67](https://etherscan.io/address/0x477c1b7dc1091389cbd3eef21efb00081606ab67) | Occasional User - Low Impact | 3.0K | 120 | 25 | 1 | 13.5% | 22,235 | 25,235 |
| 30 | [0x3cbe03d5bfc55b47e332b9ff71feba0f0e2133dd](https://etherscan.io/address/0x3cbe03d5bfc55b47e332b9ff71feba0f0e2133dd) | Occasional User - Low Impact | 2,700 | 150 | 18 | 1 | 19.4% | 13,941 | 16,641 |
| 31 | [0x221bcf9ccece1452edd113839be1740433910f6c](https://etherscan.io/address/0x221bcf9ccece1452edd113839be1740433910f6c) | Occasional User - Low Impact | 1,800 | 150 | 12 | 1 | 19.4% | 9,294 | 11,094 |
| 32 | [0xbb57444579afde79b11a51e0a91d1dc1a9742f90](https://etherscan.io/address/0xbb57444579afde79b11a51e0a91d1dc1a9742f90) | Rare User - Low Impact | 1,800 | 225 | 8 | 1 | 46.2% | 3,898 | 5,698 |
| 33 | [0x686d2493ce60e2f3b2f49979611f3246fdbcf3ec](https://etherscan.io/address/0x686d2493ce60e2f3b2f49979611f3246fdbcf3ec) | Rare User - Low Impact | 1,500 | 300 | 5 | 1 | 150.0% | 1.0K | 2,500 |
| 34 | [0x9a5e3cd9c92c455a1fcf4acd52068f1dd3ec3998](https://etherscan.io/address/0x9a5e3cd9c92c455a1fcf4acd52068f1dd3ec3998) | Rare User - Low Impact | 1,200 | 300 | 4 | 1 | 150.0% | 800 | 2.0K |
| 35 | [0x0eae98ccfeed226f7f8cbe647612f7795d638e3b](https://etherscan.io/address/0x0eae98ccfeed226f7f8cbe647612f7795d638e3b) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 36 | [0x2bc3ae0a4f2d91471c3484996d2d690348f91a59](https://etherscan.io/address/0x2bc3ae0a4f2d91471c3484996d2d690348f91a59) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 37 | [0x38d26f67e3b15ccef9544cf960211f718915487b](https://etherscan.io/address/0x38d26f67e3b15ccef9544cf960211f718915487b) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 38 | [0x4d175a2bd7c081c18ef2e32a30dfef228241f152](https://etherscan.io/address/0x4d175a2bd7c081c18ef2e32a30dfef228241f152) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 39 | [0x6300cfda24b465e63871672558957be137fdb7df](https://etherscan.io/address/0x6300cfda24b465e63871672558957be137fdb7df) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 40 | [0x7b9bae375447aa3905bd6b90ed588195404e3f6e](https://etherscan.io/address/0x7b9bae375447aa3905bd6b90ed588195404e3f6e) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 41 | [0xeae902641749fa54d9d0f90932033e8ca47c966a](https://etherscan.io/address/0xeae902641749fa54d9d0f90932033e8ca47c966a) | Rare User - Low Impact | 300 | 300 | 1 | 1 | 150.0% | 200 | 500 |
| 42 | [0x000097d4a261d7ad074089ca08efa2b136aa6d38](https://etherscan.io/address/0x000097d4a261d7ad074089ca08efa2b136aa6d38) | Occasional User - Low Impact | 0 | 0 | 15 | 1 | 0.0% | 20,070 | 20,070 |
| 43 | [0x01b27db5a9a57c7bd411676413980f0c5ac2fd4f](https://etherscan.io/address/0x01b27db5a9a57c7bd411676413980f0c5ac2fd4f) | Regular User - Low Impact | 0 | 0 | 105 | 1 | 0.0% | 142,800 | 142,800 |
| 44 | [0x0392b4cc79fbb0f38d8942866c0302ae01c2b194](https://etherscan.io/address/0x0392b4cc79fbb0f38d8942866c0302ae01c2b194) | Occasional User - Low Impact | 0 | 0 | 69 | 1 | 0.0% | 93,840 | 93,840 |
| 45 | [0x0928dabedea331ea20780e5aa6309fa8fd7f20e1](https://etherscan.io/address/0x0928dabedea331ea20780e5aa6309fa8fd7f20e1) | Rare User - Low Impact | 0 | 0 | 2 | 1 | 0.0% | 2,720 | 2,720 |
| 46 | [0x0a0256a9166041101c90be87bbebb8242a3ba015](https://etherscan.io/address/0x0a0256a9166041101c90be87bbebb8242a3ba015) | Occasional User - Low Impact | 0 | 0 | 45 | 1 | 0.0% | 61,200 | 61,200 |
| 47 | [0x0e902b2d0408754271c9e97d81fd2ede279cade6](https://etherscan.io/address/0x0e902b2d0408754271c9e97d81fd2ede279cade6) | Occasional User - Low Impact | 0 | 0 | 99 | 1 | 0.0% | 134,640 | 134,640 |
| 48 | [0x10314ac278aa9d431701f49e70273bd6e40c93f7](https://etherscan.io/address/0x10314ac278aa9d431701f49e70273bd6e40c93f7) | Occasional User - Low Impact | 0 | 0 | 48 | 1 | 0.0% | 65,280 | 65,280 |
| 49 | [0x106b67c3f6d4fff429668b0496d2e4cda55e805b](https://etherscan.io/address/0x106b67c3f6d4fff429668b0496d2e4cda55e805b) | Occasional User - Low Impact | 0 | 0 | 48 | 1 | 0.0% | 65,280 | 65,280 |
| 50 | [0x119bded2b517c58f4b6d22b91610ca57d1a02fb0](https://etherscan.io/address/0x119bded2b517c58f4b6d22b91610ca57d1a02fb0) | Rare User - Low Impact | 0 | 0 | 1 | 1 | 0.0% | 1,349 | 1,349 |

## Entity Activity Patterns

### Most Active Entities

| Rank | Address | Total Calls | Active Blocks | Calls/1K Blocks | First Block | Last Block | Activity Span |
|------|---------|-------------|---------------|-----------------|-------------|------------|---------------|
| 1 | [0x0000...4a5f](https://etherscan.io/address/0x000000629fbcf27a347d1aeba658435230d74a5f) | 9,378 | 1,555 | 19.1 | 22.09M | 22.58M | 491,249 blocks |
| 2 | [0xaaf7...67d9](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | 8,001 | 292 | 18.4 | 22.09M | 22.52M | 434,337 blocks |
| 3 | [0x54ab...659a](https://etherscan.io/address/0x54ab716d465be3d5eeca64e63ac0048d7a81659a) | 7,440 | 688 | 17.1 | 22.09M | 22.52M | 434,429 blocks |
| 4 | [0xfcb7...9c0d](https://etherscan.io/address/0xfcb73f6405f6b9be91013d9477d81833a69c9c0d) | 4,146 | 691 | 8.4 | 22.09M | 22.58M | 491,230 blocks |
| 5 | [0xf3b0...ce1f](https://etherscan.io/address/0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f) | 3,338 | 335 | 7.7 | 22.09M | 22.52M | 434,405 blocks |
| 6 | [0x7202...7db9](https://etherscan.io/address/0x7202932b3be70edf0657d5bada261d610e0d7db9) | 3,057 | 967 | 30.6 | 22.09M | 22.19M | 99,858 blocks |
| 7 | [0x454e...ca4e](https://etherscan.io/address/0x454ef2f69f91527856e06659f92a66f464c1ca4e) | 2,685 | 1,342 | 5.5 | 22.09M | 22.58M | 491,392 blocks |
| 8 | [0x58d1...6522](https://etherscan.io/address/0x58d14960e0a2be353edde61ad719196a2b816522) | 1,571 | 192 | 3.2 | 22.09M | 22.58M | 490,906 blocks |
| 9 | [0x3527...2092](https://etherscan.io/address/0x3527439923a63f8c13cf72b8fe80a77f6e572092) | 1,113 | 144 | 3.1 | 22.09M | 22.45M | 359,712 blocks |
| 10 | [0x2b71...6e0d](https://etherscan.io/address/0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d) | 1,104 | 138 | 2.3 | 22.09M | 22.58M | 486,104 blocks |
| 11 | [0x4337...8084](https://etherscan.io/address/0x4337001fff419768e088ce247456c1b892888084) | 1,021 | 502 | 2.1 | 22.09M | 22.58M | 491,205 blocks |
| 12 | [0x4337...8d0e](https://etherscan.io/address/0x4337003fcd2f56de3977ccb806383e9161628d0e) | 999 | 490 | 2.0 | 22.09M | 22.58M | 491,296 blocks |
| 13 | [0x4337...a93d](https://etherscan.io/address/0x4337002c5702ce424cb62a56ca038e31e1d4a93d) | 975 | 482 | 2.0 | 22.09M | 22.58M | 491,380 blocks |
| 14 | [0x4337...98b6](https://etherscan.io/address/0x4337005db25dbad41da5692ba1188751ee5d98b6) | 952 | 469 | 1.9 | 22.09M | 22.58M | 491,140 blocks |
| 15 | [0x4337...9e5d](https://etherscan.io/address/0x4337004ec9c1417f1c7a26ebd4b4fbed6acf9e5d) | 951 | 468 | 1.9 | 22.09M | 22.58M | 491,211 blocks |
| 16 | [0xc2ad...a474](https://etherscan.io/address/0xc2adcfccee33a417064d1a45d3b202de6d9fa474) | 822 | 137 | 1.7 | 22.09M | 22.58M | 490,826 blocks |
| 17 | [0x9c0b...afdc](https://etherscan.io/address/0x9c0b0dbbae8a976ceea8c2a96f6d00c53839afdc) | 750 | 125 | 1.5 | 22.09M | 22.58M | 490,993 blocks |
| 18 | [0x94a3...ac05](https://etherscan.io/address/0x94a365ca808029af8db18257ecd296c16c61ac05) | 645 | 101 | 1.6 | 22.09M | 22.50M | 411,508 blocks |
| 19 | [0x6f9d...ec2c](https://etherscan.io/address/0x6f9d816c4ec365fe8fc6898c785be0e2d51bec2c) | 525 | 175 | 1.1 | 22.09M | 22.58M | 490,988 blocks |
| 20 | [0x52ff...6754](https://etherscan.io/address/0x52ff08f313a00a54e3beffb5c4a7f7446efb6754) | 384 | 64 | 0.8 | 22.09M | 22.58M | 489,834 blocks |

### Highest Average Impact per Call

| Rank | Address | Avg Increase/Call | Total Calls | Total Increase | Category |
|------|---------|-------------------|-------------|----------------|----------|
| 1 | [0xfe32...6d2f](https://etherscan.io/address/0xfe325f97146124f3767bfa59899fa4177fd46d2f) | 300 | 47 | 14,100 | Occasional User - Medium Impact |
| 2 | [0x01c3...f91e](https://etherscan.io/address/0x01c3a1a6890a146ac187a019f9863b3ab2bff91e) | 240 | 205 | 49,200 | Regular User - Medium Impact |
| 3 | [0x0f9b...cb2f](https://etherscan.io/address/0x0f9b807d5b0ce12450059b425dc35c727d65cb2f) | 225 | 136 | 30,600 | Regular User - Medium Impact |
| 4 | [0x2572...169d](https://etherscan.io/address/0x2572835e02b59078711aa0800490e80975e4169d) | 225 | 168 | 37,800 | Regular User - Medium Impact |
| 5 | [0x2b71...6e0d](https://etherscan.io/address/0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d) | 225 | 1,104 | 248,400 | Frequent User - High Impact |
| 6 | [0x59b8...c210](https://etherscan.io/address/0x59b84b24e307682df830b32ddc826fbbe003c210) | 225 | 144 | 32,400 | Regular User - Medium Impact |
| 7 | [0x7fea...e0b7](https://etherscan.io/address/0x7fea26a181a792b5107ee0a31e434f5dbcbbe0b7) | 225 | 32 | 7,200 | Occasional User - Low Impact |
| 8 | [0xb66d...9e67](https://etherscan.io/address/0xb66d4af4e96bf96026454a6a150edd2ce55e9e67) | 225 | 16 | 3,600 | Occasional User - Low Impact |
| 9 | [0xb9d4...4122](https://etherscan.io/address/0xb9d48daf26f3cbe01a959f09f98e8a2ec8204122) | 225 | 16 | 3,600 | Occasional User - Low Impact |
| 10 | [0xaaf7...67d9](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | 224.67 | 8,001 | 1.80M | Heavy User - High Impact |
| 11 | [0xf3b0...ce1f](https://etherscan.io/address/0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f) | 223.43 | 3,338 | 745,800 | Frequent User - High Impact |
| 12 | [0x54ab...659a](https://etherscan.io/address/0x54ab716d465be3d5eeca64e63ac0048d7a81659a) | 223.31 | 7,440 | 1.66M | Heavy User - High Impact |
| 13 | [0x58d1...6522](https://etherscan.io/address/0x58d14960e0a2be353edde61ad719196a2b816522) | 219.99 | 1,571 | 345,600 | Frequent User - High Impact |
| 14 | [0x3527...2092](https://etherscan.io/address/0x3527439923a63f8c13cf72b8fe80a77f6e572092) | 218.87 | 1,113 | 243,600 | Frequent User - High Impact |
| 15 | [0xad0a...2d2a](https://etherscan.io/address/0xad0a80a085095eca46de3053c345516f1c722d2a) | 209.71 | 309 | 64,800 | Regular User - Medium Impact |
| 16 | [0x0000...4a5f](https://etherscan.io/address/0x000000629fbcf27a347d1aeba658435230d74a5f) | 150 | 9,378 | 1.41M | Heavy User - High Impact |
| 17 | [0x221b...0f6c](https://etherscan.io/address/0x221bcf9ccece1452edd113839be1740433910f6c) | 150 | 12 | 1,800 | Occasional User - Low Impact |
| 18 | [0x3cbe...33dd](https://etherscan.io/address/0x3cbe03d5bfc55b47e332b9ff71feba0f0e2133dd) | 150 | 18 | 2,700 | Occasional User - Low Impact |
| 19 | [0x52ff...6754](https://etherscan.io/address/0x52ff08f313a00a54e3beffb5c4a7f7446efb6754) | 150 | 384 | 57,600 | Regular User - Medium Impact |
| 20 | [0x9c0b...afdc](https://etherscan.io/address/0x9c0b0dbbae8a976ceea8c2a96f6d00c53839afdc) | 150 | 750 | 112,500 | Regular User - High Impact |

## Top 50 Most Affected Contracts

| Rank | Contract Address | Total Increase | Avg per Call | Total Calls | Unique Users | User Concentration | % Increase | Current Cost | New Cost |
|------|------------------|----------------|--------------|-------------|--------------|-------------------|------------|--------------|----------|
| 1 | [0x8c0bfc04ada21fd496c55b8c50331f904306f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) | 2.99M | 218.56 | 13,696 | 17 | 1.00 | 42.7% | 7.01M | 10.00M |
| 2 | [0x5d8ba173dc6c3c90c8f7c04c9288bef5fdbad06e](https://etherscan.io/address/0x5d8ba173dc6c3c90c8f7c04c9288bef5fdbad06e) | 2.29M | 225 | 10,160 | 9 | 1.00 | 46.2% | 4.95M | 7.24M |
| 3 | [0x68d30f47f19c07bccef4ac7fae2dc12fca3e0dc9](https://etherscan.io/address/0x68d30f47f19c07bccef4ac7fae2dc12fca3e0dc9) | 1.41M | 150 | 9,378 | 1 | 1.00 | 19.4% | 7.26M | 8.67M |
| 4 | [0x3b4d794a66304f130a4db8f2551b0070dfcf5ca7](https://etherscan.io/address/0x3b4d794a66304f130a4db8f2551b0070dfcf5ca7) | 621,900 | 150 | 4,146 | 1 | 1.00 | 19.4% | 3.21M | 3.83M |
| 5 | [0x02993cdc11213985b9b13224f3af289f03bf298d](https://etherscan.io/address/0x02993cdc11213985b9b13224f3af289f03bf298d) | 123,300 | 150 | 822 | 1 | 1.00 | 19.4% | 636,639 | 759,939 |
| 6 | [0x7cf3876f681dbb6eda8f6ffc45d66b996df08fae](https://etherscan.io/address/0x7cf3876f681dbb6eda8f6ffc45d66b996df08fae) | 112,500 | 150 | 750 | 1 | 1.00 | 19.4% | 580,875 | 693,375 |
| 7 | [0xece9cf6a8f2768a3b8b65060925b646afeaa5167](https://etherscan.io/address/0xece9cf6a8f2768a3b8b65060925b646afeaa5167) | 75,600 | 117.21 | 645 | 1 | 1.00 | 13.1% | 577,746 | 653,346 |
| 8 | [0xd19d4b5d358258f05d7b411e21a1460d11b0876f](https://etherscan.io/address/0xd19d4b5d358258f05d7b411e21a1460d11b0876f) | 57,600 | 150 | 384 | 1 | 1.00 | 19.4% | 297,408 | 355,008 |
| 9 | [0xabea9132b05a70803a4e85094fd0e1800777fbef](https://etherscan.io/address/0xabea9132b05a70803a4e85094fd0e1800777fbef) | 49,200 | 240 | 205 | 1 | 1.00 | 55.8% | 88,109 | 137,309 |
| 10 | [0xb32cb5677a7c971689228ec835800432b339ba2b](https://etherscan.io/address/0xb32cb5677a7c971689228ec835800432b339ba2b) | 35,496 | 4,437 | 8 | 2 | 0.75 | 413.2% | 8,590 | 70,992 |
| 11 | [0x30efaaa99f8efe310d9fdc83072e2a04c093d400](https://etherscan.io/address/0x30efaaa99f8efe310d9fdc83072e2a04c093d400) | 14,100 | 300 | 47 | 1 | 0.98 | 150.0% | 9,400 | 23,500 |
| 12 | [0xd1ce90003a10e6dab877890ab1fd96511555e4b3](https://etherscan.io/address/0xd1ce90003a10e6dab877890ab1fd96511555e4b3) | 10,920 | 1,365 | 8 | 1 | 0.88 | 682.5% | 1,600 | 21,840 |
| 13 | [0xb45440830bd8d288bb2b5b01be303ae60fc855d8](https://etherscan.io/address/0xb45440830bd8d288bb2b5b01be303ae60fc855d8) | 10,800 | 150 | 72 | 1 | 0.99 | 19.4% | 55,764 | 66,564 |
| 14 | [0xfeda03b91514d31b435d4e1519fd9e699c29bbfc](https://etherscan.io/address/0xfeda03b91514d31b435d4e1519fd9e699c29bbfc) | 3,300 | 300 | 11 | 4 | 0.64 | 150.0% | 2,200 | 5,500 |
| 15 | [0x2f3c205613d9451f88e19e011ed23775afe00c41](https://etherscan.io/address/0x2f3c205613d9451f88e19e011ed23775afe00c41) | 2,700 | 150 | 18 | 1 | 0.94 | 19.4% | 13,941 | 16,641 |
| 16 | [0x38de07d2526ae929f1903e5f109b70c50e12a8e0](https://etherscan.io/address/0x38de07d2526ae929f1903e5f109b70c50e12a8e0) | 1,800 | 150 | 12 | 1 | 0.92 | 19.4% | 9,294 | 11,094 |
| 17 | [0xd18d17791f2071bf3c855ba770420a9edea0728d](https://etherscan.io/address/0xd18d17791f2071bf3c855ba770420a9edea0728d) | 1,200 | 300 | 4 | 4 | 0.00 | 150.0% | 800 | 2.0K |
| 18 | [0x2eb474cffabca358d9fd3f1d43ad2b2dfb809b0e](https://etherscan.io/address/0x2eb474cffabca358d9fd3f1d43ad2b2dfb809b0e) | 300 | 300 | 1 | 1 | 0.00 | 150.0% | 200 | 500 |
| 19 | [0x271682deb8c4e0901d1a1550ad2e64d568e69909](https://etherscan.io/address/0x271682deb8c4e0901d1a1550ad2e64d568e69909) | 0 | 0 | 8 | 3 | 0.62 | 0.0% | 10,792 | 10,792 |
| 20 | [0x2d5805a423d6ce771f06972ad4499f120902631a](https://etherscan.io/address/0x2d5805a423d6ce771f06972ad4499f120902631a) | 0 | 0 | 4 | 2 | 0.50 | 0.0% | 5,440 | 5,440 |
| 21 | [0x159f3668c72bbecdf1fb31beed606ec9649654eb](https://etherscan.io/address/0x159f3668c72bbecdf1fb31beed606ec9649654eb) | 0 | 0 | 1 | 1 | 0.00 | 0.0% | 1,349 | 1,349 |
| 22 | [0x1fa7cb4925086128f3bb9e26761c9c75dbac3cd1](https://etherscan.io/address/0x1fa7cb4925086128f3bb9e26761c9c75dbac3cd1) | 0 | 0 | 3 | 2 | 0.33 | 0.0% | 4,047 | 4,047 |
| 23 | [0x150fe8dbb943c372f3e8c31d9c89f1e6a13cbbfd](https://etherscan.io/address/0x150fe8dbb943c372f3e8c31d9c89f1e6a13cbbfd) | 0 | 0 | 296 | 1 | 1.00 | 0.0% | 396,048 | 396,048 |
| 24 | [0x0baac79acd45a023e19345c352d8a7a83c4e5656](https://etherscan.io/address/0x0baac79acd45a023e19345c352d8a7a83c4e5656) | 0 | 0 | 3 | 1 | 0.67 | 0.0% | 4,014 | 4,014 |
| 25 | [0x0000000071727de22e5e9d8baf0edac6f37da032](https://etherscan.io/address/0x0000000071727de22e5e9d8baf0edac6f37da032) | 0 | 0 | 252 | 7 | 0.97 | 0.0% | 342,720 | 342,720 |
| 26 | [0x3d18ad735f949febd59bbfcb5864ee0157607616](https://etherscan.io/address/0x3d18ad735f949febd59bbfcb5864ee0157607616) | 0 | 0 | 15 | 1 | 0.93 | 0.0% | 20,070 | 20,070 |
| 27 | [0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458](https://etherscan.io/address/0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458) | 0 | 0 | 22 | 1 | 0.95 | 0.0% | 29,678 | 29,678 |
| 28 | [0x9569fe8cd0050069328e3707cffb61c77ddeb9d0](https://etherscan.io/address/0x9569fe8cd0050069328e3707cffb61c77ddeb9d0) | 0 | 0 | 3 | 1 | 0.67 | 0.0% | 4,047 | 4,047 |
| 29 | [0x92ef6af472b39f1b363da45e35530c24619245a4](https://etherscan.io/address/0x92ef6af472b39f1b363da45e35530c24619245a4) | 0 | 0 | 177 | 1 | 0.99 | 0.0% | 238,773 | 238,773 |
| 30 | [0x8ddbbcc0999f396237b6534ac600ebb0d8618c99](https://etherscan.io/address/0x8ddbbcc0999f396237b6534ac600ebb0d8618c99) | 0 | 0 | 2 | 1 | 0.50 | 0.0% | 2,720 | 2,720 |
| 31 | [0x870679e138bcdf293b7ff14dd44b70fc97e12fc0](https://etherscan.io/address/0x870679e138bcdf293b7ff14dd44b70fc97e12fc0) | 0 | 0 | 2,685 | 1 | 1.00 | 0.0% | 3.59M | 3.59M |
| 32 | [0x5968ada261a84e19a6c85830e655647752585ed4](https://etherscan.io/address/0x5968ada261a84e19a6c85830e655647752585ed4) | 0 | 0 | 11 | 1 | 0.91 | 0.0% | 14,960 | 14,960 |
| 33 | [0x5b5a0580bcfd3673820bb249514234afad33e209](https://etherscan.io/address/0x5b5a0580bcfd3673820bb249514234afad33e209) | 0 | 0 | 3 | 1 | 0.67 | 0.0% | 4,080 | 4,080 |
| 34 | [0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) | 0 | 0 | 11,270 | 73 | 0.99 | 0.0% | 15.33M | 15.33M |
| 35 | [0xbadc0ffee00baa564f3fea62e9d37843284c1e6a](https://etherscan.io/address/0xbadc0ffee00baa564f3fea62e9d37843284c1e6a) | 0 | 0 | 2 | 1 | 0.50 | 0.0% | 2,720 | 2,720 |
| 36 | [0xb90ed4c123843cbfd66b11411ee7694ef37e6e72](https://etherscan.io/address/0xb90ed4c123843cbfd66b11411ee7694ef37e6e72) | 0 | 0 | 132 | 1 | 0.99 | 0.0% | 179,520 | 179,520 |
| 37 | [0xb3445d5413abf63df1112a4a517de2602f249785](https://etherscan.io/address/0xb3445d5413abf63df1112a4a517de2602f249785) | 0 | 0 | 3 | 1 | 0.67 | 0.0% | 4,080 | 4,080 |
| 38 | [0xad3b67bca8935cb510c8d18bd45f0b94f54a968f](https://etherscan.io/address/0xad3b67bca8935cb510c8d18bd45f0b94f54a968f) | 0 | 0 | 2 | 1 | 0.50 | 0.0% | 2,720 | 2,720 |
| 39 | [0xa13baf47339d63b743e7da8741db5456dac1e556](https://etherscan.io/address/0xa13baf47339d63b743e7da8741db5456dac1e556) | 0 | 0 | 525 | 1 | 1.00 | 0.0% | 708,225 | 708,225 |
| 40 | [0xd7f86b4b8cae7d942340ff628f82735b7a20893a](https://etherscan.io/address/0xd7f86b4b8cae7d942340ff628f82735b7a20893a) | 0 | 0 | 467 | 3 | 0.99 | 0.0% | 629,983 | 629,983 |
| 41 | [0xef2a435e5ee44b2041100ef8cbc8ae035166606c](https://etherscan.io/address/0xef2a435e5ee44b2041100ef8cbc8ae035166606c) | 0 | 0 | 64 | 1 | 0.98 | 0.0% | 85,632 | 85,632 |
| 42 | [0xf0d54349addcf704f77ae15b96510dea15cb7952](https://etherscan.io/address/0xf0d54349addcf704f77ae15b96510dea15cb7952) | 0 | 0 | 2 | 1 | 0.50 | 0.0% | 2,698 | 2,698 |

### Most Used Contracts by Unique Users

| Rank | Contract Address | Unique Users | Total Calls | Avg Calls/User | Total Increase |
|------|------------------|--------------|-------------|----------------|----------------|
| 1 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) | 73 | 11,270 | 154.4 | 0 |
| 2 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) | 17 | 13,696 | 805.6 | 2.99M |
| 3 | [0x5d8b...d06e](https://etherscan.io/address/0x5d8ba173dc6c3c90c8f7c04c9288bef5fdbad06e) | 9 | 10,160 | 1128.9 | 2.29M |
| 4 | [0x0000...a032](https://etherscan.io/address/0x0000000071727de22e5e9d8baf0edac6f37da032) | 7 | 252 | 36.0 | 0 |
| 5 | [0xd18d...728d](https://etherscan.io/address/0xd18d17791f2071bf3c855ba770420a9edea0728d) | 4 | 4 | 1.0 | 1,200 |
| 6 | [0xfeda...bbfc](https://etherscan.io/address/0xfeda03b91514d31b435d4e1519fd9e699c29bbfc) | 4 | 11 | 2.8 | 3,300 |
| 7 | [0x2716...9909](https://etherscan.io/address/0x271682deb8c4e0901d1a1550ad2e64d568e69909) | 3 | 8 | 2.7 | 0 |
| 8 | [0xd7f8...893a](https://etherscan.io/address/0xd7f86b4b8cae7d942340ff628f82735b7a20893a) | 3 | 467 | 155.7 | 0 |
| 9 | [0x1fa7...3cd1](https://etherscan.io/address/0x1fa7cb4925086128f3bb9e26761c9c75dbac3cd1) | 2 | 3 | 1.5 | 0 |
| 10 | [0x2d58...631a](https://etherscan.io/address/0x2d5805a423d6ce771f06972ad4499f120902631a) | 2 | 4 | 2.0 | 0 |
| 11 | [0xb32c...ba2b](https://etherscan.io/address/0xb32cb5677a7c971689228ec835800432b339ba2b) | 2 | 8 | 4.0 | 35,496 |
| 12 | [0x0299...298d](https://etherscan.io/address/0x02993cdc11213985b9b13224f3af289f03bf298d) | 1 | 822 | 822.0 | 123,300 |
| 13 | [0x0baa...5656](https://etherscan.io/address/0x0baac79acd45a023e19345c352d8a7a83c4e5656) | 1 | 3 | 3.0 | 0 |
| 14 | [0x150f...bbfd](https://etherscan.io/address/0x150fe8dbb943c372f3e8c31d9c89f1e6a13cbbfd) | 1 | 296 | 296.0 | 0 |
| 15 | [0x159f...54eb](https://etherscan.io/address/0x159f3668c72bbecdf1fb31beed606ec9649654eb) | 1 | 1 | 1.0 | 0 |
| 16 | [0x2eb4...9b0e](https://etherscan.io/address/0x2eb474cffabca358d9fd3f1d43ad2b2dfb809b0e) | 1 | 1 | 1.0 | 300 |
| 17 | [0x2f3c...0c41](https://etherscan.io/address/0x2f3c205613d9451f88e19e011ed23775afe00c41) | 1 | 18 | 18.0 | 2,700 |
| 18 | [0x30ef...d400](https://etherscan.io/address/0x30efaaa99f8efe310d9fdc83072e2a04c093d400) | 1 | 47 | 47.0 | 14,100 |
| 19 | [0x38de...a8e0](https://etherscan.io/address/0x38de07d2526ae929f1903e5f109b70c50e12a8e0) | 1 | 12 | 12.0 | 1,800 |
| 20 | [0x3b4d...5ca7](https://etherscan.io/address/0x3b4d794a66304f130a4db8f2551b0070dfcf5ca7) | 1 | 4,146 | 4146.0 | 621,900 |

## Entity Relationships

### Multi-Contract Users

Entities using multiple contracts (top 20 by total impact):

| Rank | Entity Address | Contracts Used | Total Calls | Total Increase | Primary Contract |
|------|----------------|----------------|-------------|----------------|------------------|
| 1 | [0xaaf7...67d9](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | 2 | 8,001 | 1.80M | [0x5d8b...d06e](https://etherscan.io/address/0x5d8ba173dc6c3c90c8f7c04c9288bef5fdbad06e) |
| 2 | [0x54ab...659a](https://etherscan.io/address/0x54ab716d465be3d5eeca64e63ac0048d7a81659a) | 2 | 7,440 | 1.66M | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 3 | [0xf3b0...ce1f](https://etherscan.io/address/0xf3b07f6744e06cd5074b7d15ed2c33760837ce1f) | 2 | 3,338 | 745,800 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 4 | [0x58d1...6522](https://etherscan.io/address/0x58d14960e0a2be353edde61ad719196a2b816522) | 2 | 1,571 | 345,600 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 5 | [0x2b71...6e0d](https://etherscan.io/address/0x2b711ee00b50d67667c4439c28aeaf7b75cb6e0d) | 2 | 1,104 | 248,400 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 6 | [0x2572...169d](https://etherscan.io/address/0x2572835e02b59078711aa0800490e80975e4169d) | 2 | 168 | 37,800 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 7 | [0x59b8...c210](https://etherscan.io/address/0x59b84b24e307682df830b32ddc826fbbe003c210) | 2 | 144 | 32,400 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 8 | [0x0f9b...cb2f](https://etherscan.io/address/0x0f9b807d5b0ce12450059b425dc35c727d65cb2f) | 2 | 136 | 30,600 | [0x8c0b...f564](https://etherscan.io/address/0x8c0bfc04ada21fd496c55b8c50331f904306f564) |
| 9 | [0x4337...8084](https://etherscan.io/address/0x4337001fff419768e088ce247456c1b892888084) | 2 | 1,021 | 0 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) |
| 10 | [0x4337...a93d](https://etherscan.io/address/0x4337002c5702ce424cb62a56ca038e31e1d4a93d) | 2 | 975 | 0 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) |
| 11 | [0x4337...8d0e](https://etherscan.io/address/0x4337003fcd2f56de3977ccb806383e9161628d0e) | 2 | 999 | 0 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) |
| 12 | [0x4337...98b6](https://etherscan.io/address/0x4337005db25dbad41da5692ba1188751ee5d98b6) | 2 | 952 | 0 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) |
| 13 | [0x4337...9e5d](https://etherscan.io/address/0x4337004ec9c1417f1c7a26ebd4b4fbed6acf9e5d) | 2 | 951 | 0 | [0x5ff1...2789](https://etherscan.io/address/0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789) |
| 14 | [0x5ccc...aa54](https://etherscan.io/address/0x5ccc2130e77ae3a3211740c2e897bfbb5d70aa54) | 2 | 2 | 0 | [0x1fa7...3cd1](https://etherscan.io/address/0x1fa7cb4925086128f3bb9e26761c9c75dbac3cd1) |

## Power User Analysis

Entities in the top 1% by call volume (≥7,765 calls):

| Rank | Address | Total Calls | Total Increase | % of All Calls | % of All Increase | Category |
|------|---------|-------------|----------------|----------------|-------------------|----------|
| 1 | [0x0000...4a5f](https://etherscan.io/address/0x000000629fbcf27a347d1aeba658435230d74a5f) | 9,378 | 1.41M | 16.65% | 18.02% | Heavy User - High Impact |
| 2 | [0xaaf7...67d9](https://etherscan.io/address/0xaaf7b278bac078aa4f9bdc8e0a93cde604aa67d9) | 8,001 | 1.80M | 14.21% | 23.03% | Heavy User - High Impact |

## Summary Statistics

### Entity Distribution

- **Heavy Users (≥5,000 calls)**: 3 entities
- **Frequent Users (1,000-4,999 calls)**: 8 entities
- **Regular Users (100-999 calls)**: 27 entities
- **Occasional Users (10-99 calls)**: 66 entities
- **Rare Users (<10 calls)**: 39 entities

### Impact Distribution

- **High Impact (≥100K gas increase)**: 10 entities
- **Medium Impact (10K-99K gas)**: 15 entities
- **Low Impact (<10K gas)**: 118 entities

### Concentration Metrics

- **Top 10 entities**: 93.6% of total gas increase
- **Top 50 entities**: 100.0% of total gas increase
- **Top 100 entities**: 100.0% of total gas increase

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
