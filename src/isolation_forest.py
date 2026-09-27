import numpy as np
import pandas as pd

from typing import List

from isolation_tree import Isolation_Tree

class Isolation_Forest:
    def __init__(self, df: pd.DataFrame, sample_size: int, n_estimators: int, max_depth: int):
        self.df: pd.DataFrame = df
        self.sample_size: int = sample_size
        self.n_estimators: int = n_estimators
        self.trees: List[Isolation_Tree] = self.build_ensemble(df, max_depth)

    def random_sample(self, data_set: pd.DataFrame) -> List[pd.DataFrame]:
        """
        Returns a random sample of a dataset for isolation.
        """
        sample_size: int = self.sample_size
        sample_list: List[pd.DataFrame] = []

        for _ in range(0, self.n_estimators):
            samples: List[pd.Series] = []
            df_shuffled: pd.DataFrame = data_set.sample(frac=1,
                                                        random_state=42 + len(sample_list)
                                                        ).reset_index(drop=True)
            for j in range(0, sample_size):
                samples.append(df_shuffled.iloc[j])

            df: pd.DataFrame = pd.DataFrame(samples)
            sample_list.append(df)

        return sample_list

    def build_ensemble(self, data_set: pd.DataFrame, max_depth: int) -> List[Isolation_Tree]:
        """
        Builds an Isolation Tree for each sampled dataset.
        """
        sample_list: List[pd.DataFrame] = self.random_sample(data_set)
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

        average: float = sum(lengths) / len(lengths)
        
        return average

    def anomaly_score(self, row: pd.Series) -> float:
        """
        Converts average into an anomaly score.
        """
        c_sample: float = self.trees[0].expected_extra_length(self.sample_size)
        average: float = self.average_path_length(row)

        ratio: float = 2 ** (-average / c_sample)

        return ratio
