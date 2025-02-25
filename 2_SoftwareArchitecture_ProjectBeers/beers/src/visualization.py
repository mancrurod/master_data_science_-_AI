import seaborn as sns
import pandas as pd
import matplotlib.pyplot as pyplot

def visualize_data_original(df):
    # Show the distribution of the style of beers. Use pie chart when % > 2
    style_distribution = df["style"].value_counts(normalize=True)
    style_distribution = style_distribution[style_distribution > 0.02]
    style_distribution["other"] = 1 - style_distribution.sum()
    style_distribution.plot.pie(autopct="%1.1f%%")
    pyplot.savefig("images/beer_style_distribution.png")
    pyplot.show();

# Show beer style distribution when count > 5
def visualize_data_grouped(df_grouped):
    sns.histplot(data=df_grouped[df_grouped["count"] > 5], x="state", y="count", hue="style", multiple="stack")
    pyplot.savefig("images/beer_style_distribution_grouped.png")
    pyplot.show();
