import numpy as np
import pandas as pd
import random

from sklearn.datasets import load_iris

#Load Iris as dataframe (easier to work with)
iris = load_iris(as_frame=True)

iris_data = iris.data

#print(iris_data.head())

class Isolation_Tree:
    def __init__(self, df: pd.DataFrame, max_depth: int):
        self.df = df
        self.max_depth = max_depth
        self.path_length = 0

    def pick_random_feature(self) -> str:
        """
        Picks a random feature for the isolation tree.
        """
        features = [feature for feature in self.df.columns]
        rand_features = random.choice(features)
        return rand_features

    def split_values_A(self, selected_instances):
         lowest_int = selected_instances - (selected_instances - 1)
         highest_int = selected_instances
         rand_split = random.randint(lowest_int, highest_int)
         return rand_split

    def split_values_B(self, lower_range, higher_range):
        rand_split = random.randint(lower_range, higher_range)
        return rand_split

    def parition_data(self, select_feature, split_value) -> np.array:
        left_node = np.array([])
        right_node = np.array([])
        for value in self.df[select_feature].values:
            if value < split_value:
                left_node = np.append(left_node, value)
            if value >= split_value:
                right_node = np.append(right_node, value)
        return left_node, right_node

    def build_tree(self):
        rand_feature = self.pick_random_feature()
        feature_instances = int(self.df[rand_feature].values.shape[0])
        rand_split = self.split_values_A(feature_instances)
        left_node, right_node = self.parition_data(rand_feature, rand_split)
        self.path_length += 1
        self.recursive_check(left_node, right_node)

    def recursive_pass(self, left_node, right_node):
        if left_node.shape or right_node.shape == 1:
            return False

        if self.path_length == self.max_depth:
            return False

tree: Isolation_Tree = Isolation_Tree(iris_data, max_depth=3)

print(type(iris_data['petal length (cm)'].values))

e = tree.pick_random_feature()
f = tree.split_values_A(50)
left, right = tree.parition_data('petal length (cm)', 2)
s = tree.recursive_check(left, right)
c = tree.build_tree()

print(c)