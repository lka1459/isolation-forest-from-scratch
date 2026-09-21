# Isolation Forest

A lightweight, educational implementation of an isolation tree inspired by the Isolation Forest anomaly detection algorithm. This project is intended as a learning exercise and prototype for understanding how random partitioning can isolate anomalies in tabular data.

## Overview

The current implementation in [src/isolation_tree.py](src/isolation_tree.py) demonstrates the core idea behind isolation-based anomaly detection:

- randomly choose a feature
- choose a random split value within that feature's range
- partition the data into left and right branches
- track recursive tree depth and path length (working on it)
- use the Iris dataset as a simple demonstration dataset

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
pip install scikit-learn
```