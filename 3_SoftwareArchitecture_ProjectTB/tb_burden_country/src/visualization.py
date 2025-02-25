import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def show_ten_countries_most_deaths(df):
    df_plot_1 = df.groupby('Country or territory name')['Estimated number of deaths from TB (all forms, excluding HIV)'].max().sort_values(ascending=False).head(10)
    df_plot_1.plot(kind='bar')
    plt.title('Top 10 countries with most deaths from TB')
    plt.xlabel('Country')
    plt.ylabel('Number of deaths')
    plt.xticks(rotation=45, ha='right')
    plt.savefig('images/top_ten_countries_most_deaths.png')
    plt.show();

def show_top_regions_most_cases(df):
    df_plot_2 = df.groupby('Region')['Estimated number of incident cases (all forms)'].max().sort_values(ascending=False)
    plt.title('Top regions with most incident cases of TB')
    df_plot_2.plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel('Region')
    plt.savefig('images/top_regions_most_cases.png')
    plt.show();