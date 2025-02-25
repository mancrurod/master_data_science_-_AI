import seaborn as sns
import matplotlib.pyplot as plt

def age_histogram(df):
    sns.histplot(df["age"], bins=30)
    plt.title("Distribución de la edad")
    plt.savefig("images/age_histogram.png")
    plt.show();

def survival_plot(df):
    sns.countplot(data=df, x="sex", hue="survived")
    plt.title("Cantidad de supervivientes")
    plt.savefig("images/survival_plot.png")
    plt.show();