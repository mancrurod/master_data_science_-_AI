# Titanic Project

This project aims to analyze and visualize the data from the famous Titanic disaster. We use Python and various libraries for data manipulation, transformation, and visualization.

## Project Structure

The project structure is as follows:

```
titanic/
│
├── data/                   # Folder to store processed data
├── images/                 # Folder to store generated visualizations
├── src/                    # Source code
│   ├── __init__.py         # Module initialization file
│   ├── exploration.py      # Functions to explore the dataset
│   ├── transformation.py   # Functions to transform the dataset
│   ├── visualization.py    # Functions to visualize the dataset
│
├── environment.yml         # File to create the environment with conda
├── main.py                 # Main script to run the analysis
├── requirements.txt        # Requirements file for pip
└── README.md               # Project explanation
```

## Installation

To install the project dependencies, you can use `conda` or `pip`.

### Using Conda

```bash
conda env create -f environment.yml
conda activate titanic
```

### Using Pip

```bash
pip install -r requirements.txt
```

## Usage

To run the analysis, simply execute the `main.py` script:

```bash
python main.py
```

This script will perform the following actions:

1. Load the Titanic dataset.
2. Explore the dataset by displaying general information and descriptive statistics.
3. Transform the dataset by cleaning null data and creating new columns.
4. Visualize the dataset by generating graphs and saving them in the `images` folder.
5. Save the processed dataset in the `data` folder.

## Functions

### Exploration

Exploration functions are located in `src/exploration.py`:

- `describe_dataset(df)`: Displays general information and descriptive statistics of the dataset.

### Transformation

Transformation functions are located in `src/transformation.py`:

- `transform_age_sex(df)`: Creates new columns to group ages and convert sex to numerical values.
- `clean_df(df)`: Removes unnecessary columns from the dataset.
- `fill_na_age(df)`: Fills null values in the `age` column with the mean age.

### Visualization

Visualization functions are located in `src/visualization.py`:

- `age_histogram(df)`: Generates a histogram of the age distribution.
- `survival_plot(df)`: Generates a bar chart showing the number of survivors by sex.