import numpy as np
import pandas as pd
import random

from typing import List, Dict
from sklearn.datasets import load_iris

from isolation_tree import Isolation_Tree

#Load Iris as dataframe (easier to work with)
iris = load_iris(as_frame=True)

iris_data: pd.DataFrame = iris.data

class IsolationForest:
    def __init__(self, df, sample_size, n_estimators, max_depth):
        self.df = df
        self.sample_size = sample_size
        self.n_estimators = n_estimators
        self.trees: List[Isolation_Tree] = self.build_ensemble(df, max_depth)

    def random_sample(self, data_set: pd.DataFrame) -> List[pd.DataFrame]:
        """
        Returns a random sample of a dataset for isolation.
        """
        sample_size: int = self.sample_size
        sample_list: List[pd.DataFrame] = []

        for _ in range(0, self.n_estimators):
            samples: List[pd.Series] = []
            df_shuffled: pd.DataFrame = data_set.sample(frac=1).reset_index(drop=True)
            for j in range(0, sample_size):
                samples.append(df_shuffled.iloc[j])

            df: pd.DataFrame = pd.DataFrame(samples)
            sample_list.append(df)

        return sample_list

    def build_ensemble(self, data_set, max_depth: int) -> List[Isolation_Tree]:
        """
        Builds an Isolation Tree for each sampled dataset.
        """
        sample_list = self.random_sample(data_set)
        tree_list: List[Isolation_Tree] = []

        for sample in sample_list:
            isolation_tree: Isolation_Tree = Isolation_Tree(sample, max_depth)
            tree_list.append(isolation_tree)

        return tree_list

    def average_path_length(self, row: pd.Series) -> float:
        """
        Return the average path length of the Isolation Tree forest.
        """
        lengths: List[float] = []
    
        for tree in self.trees:
            lengths.append(tree.return_path_length(row))

        average = sum(lengths) / len(lengths)
        
        return average

    def anomaly_score(self, row: pd.Series):
        """
        Converts average into an anomaly score.
        """
        c_sample = self.trees[0].expected_extra_length(self.sample_size)
        average = self.average_path_length(row)

        ratio = 2 ** (-average / c_sample)

        return ratio


tree: IsolationForest = IsolationForest(iris_data, sample_size=100, n_estimators=10, max_depth=3)

e = tree.average_path_length(iris_data.iloc[0])
z = tree.anomaly_score(iris_data.iloc[10])

