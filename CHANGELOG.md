# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.1.1] - 2026-09-23

### Added
- Added typing for clearer variable declarations
- Added a stop condition based on max depth and node size

### Changed
- Changed the Iris data assignment to a typed pandas DataFrame
- Reworked the split logic to use the current node’s feature values instead of a generic integer range
- Switched the partitioning method to split actual DataFrame subsets into left and right child nodes
- Replaced the placeholder recursion logic with a recursive tree-building flow

## [0.1.0] - 2026-09-21

### Added
- Initial `Isolation_Tree` implementation in [src/isolation_tree.py](src/isolation_tree.py)
- Random feature selection and split threshold logic
- Data partitioning into left and right branches
- Basic recursive depth tracking scaffold
- Iris dataset demonstration workflow for exploratory testing
- Initial project files: [README.md](README.md), [CHANGELOG.md](CHANGELOG.md), and [requirements.txt](requirements.txt)