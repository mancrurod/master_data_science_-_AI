import seaborn as sns
import pandas as pd
import matplotlib.pyplot as pyplot

import src.exploration as exp
import src.transformation as tf
import src.visualization as vis

# Load data
df = pd.read_csv('data/TB_Burden_Country.csv')
print(f"Data loaded successfully.")

# Explore data
exp.explore_data(df)
print(f"Exploration completed.")

# Transform data
new_df = tf.transform_data(df)
print(f"Transformed dataset contains {new_df.shape[0]} rows and {new_df.shape[1]} columns.")

# Visualize data
vis.show_ten_countries_most_deaths(new_df)
vis.show_top_regions_most_cases(new_df)
print(f"Visualization completed. You can find the images in the images folder.")


