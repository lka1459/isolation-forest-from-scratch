# Isolation Forest

A lightweight, educational implementation of an isolation tree inspired by the Isolation Forest anomaly detection algorithm. This project is intended as a learning exercise and prototype for understanding how random partitioning can isolate anomalies in tabular data.

## How It Works

Each isolation tree repeatedly:

1. Chooses a feature that varies among the rows at the current node.
2. Selects a random split value within that feature's range.
3. Sends rows to left and right child nodes.
4. Stops when a row is isolated, the maximum depth is reached, or the remaining rows cannot be separated.

A new flow follows the stored splits to a leaf. Its path length is the number of edges travelled, plus an expected-length correction if multiple training rows remain in that leaf.

The forest builds several trees from different random samples and averages their corrected path lengths. Shorter average paths produce higher anomaly scores, meaning the flow is more unusual relative to the training data.

## Dataset

The project uses the [UNSW-NB15 dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset), created by UNSW Canberra for network intrusion detection research. It contains normal network traffic and several attack categories.

The published training and testing partitions used here contain:

| Partition | Network flows |
|---|---:|
| Training | 175,341 |
| Testing | 82,332 |

Each row represents a network flow. The `label` column marks normal traffic as `0` and attack traffic as `1`. `attack_cat` identifies the attack category. 

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
pip install scikit-learn
```