import numpy as np
import pandas as pd
import random

from typing import List
from sklearn.datasets import load_iris

#Load Iris as dataframe (easier to work with)
iris = load_iris(as_frame=True)

iris_data: pd.DataFrame = iris.data

class Isolation_Tree:
    def __init__(self, df: pd.DataFrame, max_depth: int):
        self.df: pd.DataFrame = df
        self.max_depth: int = max_depth
        self.path_length: int = 0

    def pick_random_feature(self) -> str:
        """
        Picks a random feature for the isolation tree.
        """
        features: List[str] = [feature for feature in self.df.columns]
        rand_features: str = random.choice(features)
        return rand_features

    def split_values(self, feature: str, data: pd.DataFrame) -> int:
         """
         Splits the instances of a node randomly.
         """
         lowest_int: np.float64  = data[feature].min()
         highest_int: np.float64 = data[feature].max()
         rand_split: int = random.uniform(lowest_int, highest_int)
         return rand_split

    def parition_data(self, node_data: pd.DataFrame, select_feature: str, split_value: int):
        """
        Partitions the data of the selected parent node into two child nodes.
        """
        left_node: pd.DataFrame = node_data[node_data[select_feature] < split_value]
        right_node: pd.DataFrame = node_data[node_data[select_feature] >= split_value]
        return left_node, right_node

    def build_tree(self, node_data: pd.DataFrame, depth: int = 0) -> None:
        """
        Build a single isolation tree based on a randomly selected feature.
        """
        if depth >= self.max_depth or len(node_data) == 1:
            return 

        print(len(node_data))

        rand_feature: str = self.pick_random_feature()      
        rand_split: int = self.split_values(rand_feature, node_data)
        left_node, right_node = self.parition_data(node_data, rand_feature, rand_split)
        self.build_tree(left_node, depth + 1)
        self.build_tree(right_node, depth + 1)
       

tree: Isolation_Tree = Isolation_Tree(iris_data, max_depth=3)

d = tree.pick_random_feature()
e = tree.split_values(d, iris_data)

b = tree.build_tree(iris_data)

print(b)