# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.2.1] - 2026-09-25

### Added
- Added an expected path length calculation for leaves containing multiple rows.
- Added a stopping condition when no features vary within a node.

### Changed
- Updated return_path_length() to add the leaf-size correction to the depth travelled by a row.
- Updated random feature selection to use only features that vary within the current node.
- Updated path traversal so each row follows exactly one child at each split.

## [0.2.0] - 2026-09-25

### Added
- Added return_path_length.

### Changed
- Changed build_tree to return nested tree dictionaries with leaf sizes, features, split values, and child nodes.
- Renamed pick_random_feature to random_feature
- Renamed parition_data to partition_data.
- Replaced path_length with a stored tree root.

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