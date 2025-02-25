import seaborn as sns
import pandas as pd
import matplotlib.pyplot as pyplot

import src.exploration as exp
import src.transformation as tf
import src.visualization as vis

# Load the data
df = pd.read_csv("data/beers.csv")

# Explore the data
exp.explore_data(df)

# Transform the data
df_grouped = tf.transform_data(df)

# Visualize the data
vis.visualize_data_original(df)
vis.visualize_data_grouped(df_grouped)


