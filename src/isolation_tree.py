import numpy as np
import pandas as pd
import random

from typing import List, Dict

class Isolation_Tree:
    def __init__(self, df: pd.DataFrame, max_depth: int):
        self.df: pd.DataFrame = df
        self.max_depth: int = max_depth
        self.root: Dict[str, str]  = self.build_tree(self.df)

    def random_feature(self, node_data: pd.DataFrame) -> str:
        """
        Picks a random feature for the isolation tree.
        """
        features: List[str] = [feature for feature in node_data.columns if node_data[feature].nunique() > 1]
        rand_features: str = random.choice(features)

        return rand_features

    def split_values(self, feature: str, data: pd.DataFrame) -> float:
        """
        Splits the instances of a node randomly.
        """
        lowest_int: np.float64  = data[feature].min()
        highest_int: np.float64 = data[feature].max()
        rand_split: float = random.uniform(lowest_int, highest_int)

        return rand_split

    def partition_data(self, node_data: pd.DataFrame, select_feature: str, split_value: float):
        """
        Partitions the data of the selected parent node into two child nodes.
        """
        left_node: pd.DataFrame = node_data[node_data[select_feature] < split_value]
        right_node: pd.DataFrame = node_data[node_data[select_feature] >= split_value]

        return left_node, right_node
                        
    def build_tree(self, node_data: pd.DataFrame, depth: int = 0) -> Dict[str, str]:
        """
        Build a single isolation tree based on a randomly selected feature.
        """
        if (
            depth >= self.max_depth 
            or len(node_data) <= 1  
            or all(node_data[col].nunique() <= 1 for col in node_data.columns)
            ):
            return {"leaf_size": len(node_data)}

        rand_feature: str = self.random_feature(node_data)      
        rand_split: float = self.split_values(rand_feature, node_data)
        left_node, right_node = self.partition_data(node_data, rand_feature, rand_split)

        return {
        "feature": rand_feature,
        "split_value": rand_split,
        "left_node": self.build_tree(left_node, depth + 1),
        "right_node": self.build_tree(right_node, depth + 1),
                }

    def return_path_length(self, row: pd.Series) -> float:
        """
        Returns path length of a row.
        """
        node: Dict[str, str] = self.root
        path_length: int = 0

        while "leaf_size" not in node:
            feature: str = node["feature"]
            split_value: int = node["split_value"]

            if row[feature] < split_value:
                node = node["left_node"]
            else:
                node = node["right_node"]
            
            path_length += 1

        leaf_size: int = node["leaf_size"]

        return path_length + self.expected_extra_length(leaf_size)

    def expected_extra_length(self, n: int) -> float:
        """
        Calculates the extra length of a path length based on leaf nodes size.
        """
        if n <= 1:
            return 0

        if n == 2:
            return 1

        harmonic: float = sum(1 / i for i in range(1, n))
        expected_length: float = (2 * harmonic) - (2 * (n - 1)/ n)
        
        return expected_length