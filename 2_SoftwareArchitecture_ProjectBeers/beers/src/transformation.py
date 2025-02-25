# Transform the data
def transform_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    # Create a new df. Group by state and style and count the number of beers
    df_grouped = df.groupby(["state", "style"]).size().reset_index(name="count")
    return df_grouped