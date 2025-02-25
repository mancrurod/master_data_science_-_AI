def describir_dataset(df):
    print(f"Este dataframe tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
    print("Información general del dataset:")
    print(df.info())
    print("\nDescripción del dataset:")
    print(df.describe())
    print("\nCantidad de valores nulos por columna:")
    print(df.isnull().sum())