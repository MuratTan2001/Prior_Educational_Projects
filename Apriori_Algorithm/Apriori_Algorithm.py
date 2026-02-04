#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from ucimlrepo import fetch_ucirepo

import numpy as np
def fetch_dataset_from_UCI(id):
    iris = fetch_ucirepo(id=id)
    X = iris.data.features
    # Replace missing values (NaNs) with 0
    X = np.nan_to_num(X, nan=0)
    # Convert dataset to binary format
    X_binary = np.array([[1 if val else 0 for val in row] for row in X])
    y = iris.data.targets
    return X_binary, y


# Function to perform frequent itemset mining using Apriori algorithm
def frequent_itemset_mining(X, min_support=0.2):
    # Convert dataset to pandas DataFrame
    df = pd.DataFrame(X)
    # Find frequent itemsets
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    return frequent_itemsets

# Function to generate association rules
def generate_association_rules(frequent_itemsets, min_threshold=0.8):
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_threshold)
    return rules

# Function to apply TF-IDF scores
def apply_tf_idf(X):
    # Calculate TF
    term_frequency = X.sum(axis=0) / len(X)
    # Calculate IDF
    inverse_document_frequency = X.astype(bool).sum(axis=0) / len(X)
    # Calculate TF-IDF
    tf_idf = term_frequency * inverse_document_frequency
    return tf_idf

# Function to save frequent itemsets to CSV
def save_frequent_itemsets_to_csv(frequent_itemsets, filename):
    frequent_itemsets.to_csv(filename, index=False)

# Function to save association rules to CSV
def save_association_rules_to_csv(rules, filename):
    rules.to_csv(filename, index=False)

# Function to save TF-IDF scores to CSV
def save_tf_idf_scores_to_csv(tf_idf_scores, filename):
    tf_idf_scores.to_csv(filename, index=False)


# Fetch dataset from UCI ML Repository
dataset_id = 53  # Update with the dataset ID you want to fetch
X, y = fetch_dataset_from_UCI(dataset_id)

# Perform frequent itemset mining using Apriori
min_support = 0.2
frequent_itemsets = frequent_itemset_mining(X, min_support)
save_frequent_itemsets_to_csv(frequent_itemsets, "frequent_itemsets.csv")

# Generate association rules
min_threshold = 0.8
rules = generate_association_rules(frequent_itemsets, min_threshold)
save_association_rules_to_csv(rules, "association_rules.csv")

# Apply TF-IDF scores
tf_idf_scores = apply_tf_idf(X)
save_tf_idf_scores_to_csv(pd.DataFrame(tf_idf_scores), "tf_idf_scores.csv")


# In[ ]:




