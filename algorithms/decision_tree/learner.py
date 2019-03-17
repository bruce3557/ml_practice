import pandas as pd

from collections import Counter


def gini_impurity(labels):
    label_counter = Counter(labels)
    total_count = len(labels)

    impurity = 0.0
    for label, cnt in label_counter.items():
        p_label = 1.0 * cnt / total_count
        impurity += p_label * (1 - p_label)
    
    print(impurity)
    return impurity


# def information_gain(labels, branched_labels):
#     total_gain = gini_impurity(labels)
#     total_num = len(labels)

#     for label_partition in branched_labels:
#         p_label_partition = 1.0 * len(label_partition) / total_num
#         branch_impurity = gini_impurity(label_partition)
#         total_gain -= branch_impurity
    
#     return total_gain

def split_df(df, branch_feature, threshold):
    if isinstance(threshold, str):
        branch_left_df = df[branch_feature == threshold]
        branch_right_df = df[branch_feature != threshold]
    elif isinstance(threshold, (int, float)):
        branch_left_df = df[branch_feature <= threshold]
        branch_right_df = df[branch_feature > threshold]
    else:
        raise Exception("Bad data type")
    
    return branch_left_df, branch_right_df


def information_gain(df, branch_feature, label_col, threshold):
    branch_left_df, branch_right_df = split_df(df, branch_feature, threshold)
    
    total_gain = gini_impurity(df[label_col]) \
        - gini_impurity(branch_left_df[label_col].tolist()) \
        - gini_impurity(branch_right_df[label_col].tolist())
    
    return total_gain


def select_threshold(df, feature, label_col):
    distinct_values = sorted(df[feature].unique().tolist()))
    best_threshold = None
    max_info_gain = float("-inf")

    for value in distinct_values:
        info_gain = information_gain(df, feature, label_col, value)
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_threshold = value

    return best_threshold, max_info_gain


def select_best_branch(df, feature_set, label_col):
    best_feature = None
    best_feature_threshold = None
    max_info_gain = float("-inf")

    for feature in feature_set:
        feature_threshold, info_gain = select_threshold(df, feature, label_col)

        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_feature = feature
            best_feature_threshold = feature_threshold

    return max_info_gain, best_feature, best_feature_threshold


class Node:
    def __init__(self):
        left = None
        right = None
        feature = None
        feature_threshold = None
        is_leaf = False
        leaf_label = None
    
    def fit(self, df, features, label_col):
        info_gain, feature, feature_threshold = select_best_branch(df, features, label_col)

        if info_gain != 0:
            self.left = Node()
            self.right = Node()
            branch_left_df, branch_right_df = split_df(df, feature, feature_threshold)
            self.left = self.left.fit(branch_left_df)
            self.right = self.right.fit(branch_right_df)
        else:
            self.is_leaf = True
            self.leaf_label = df[label_col].unique().tolist()[0]

        return self
    
    def predict(self, df):
        if self.is_leaf:
            return df.assign(pred_label=self.leaf_label)

        branch_left, branch_right = split_df(df, self.feature, self.features_threshold)
        predict_left_df = self.predict(branch_left)
        predict_right_df = self.predict(branch_right)
        
        return pd.concat([predict_left_df, predict_right_df])
        

class DecisionTree:
    def __init__(self):
        self.root = Node()

    def fit(self, df, features, label_col):
        self.root.fit(df, features, label_col)
        return self

    def predict(self, df):
        return self.root.predict(df)

