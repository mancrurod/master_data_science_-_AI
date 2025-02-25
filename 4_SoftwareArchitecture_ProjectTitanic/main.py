import seaborn as sns
import pandas as pandas

import src.exploration as exp
import src.transformation as trs
import src.visualization as viz

if __name__ == "__main__":
    print(f"Running main.py")

# Load data
df = sns.load_dataset("titanic")
print(f"Dataset loaded.")

# Exploration
print(f"Showing dataset info:")
exp.describir_dataset(df)

# Transformation
df_1 = trs.limpieza_df(df)
df_2 = trs.fill_na_age(df_1)
df_3 = trs.transformar_edad_sexo(df_2)
print(f"Dataframe has been cleaned and transformed.")

# Visualization
viz.age_histogram(df_3)
print(f"Age histogram saved in images folder.")
viz.survival_plot(df_3)
print(f"Survival plot saved in images folder.")

# Save processed data
df_3.to_csv("data/processed_titanic.csv", index=False)
print(f"Processed data saved in data folder.")
