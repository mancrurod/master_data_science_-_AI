# Beers Project

## Overview
This project is focused on analyzing and visualizing data related to various beers. The dataset includes information such as beer names, styles, breweries, and other attributes.

## Project Structure
The project is organized into the following directories and files:

- `data/`: Contains the dataset files.
  - `beers.csv`: The main dataset containing information about different beers.
- `src/`: Contains the source code for data processing and visualization.
  - `exploration.py`: Scripts for exploring the dataset.
  - `transformation.py`: Scripts for transforming the dataset.
  - `visualization.py`: Scripts for visualizing the data.
- `main.py`: The main script to run the project.
- `testing.ipynb`: Jupyter notebook for testing and experimenting with the data.

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably version 3.6 or higher).
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, you can create a conda environment using the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   conda activate beers_project
   ```
4. Run the main script to process and visualize the data:
   ```bash
   python main.py
   ```

## Data Exploration
The `exploration.py` script contains functions to load and explore the dataset. You can use this script to get an initial understanding of the data.

## Data Transformation
The `transformation.py` script includes functions to clean and transform the dataset. This is useful for preparing the data for analysis and visualization.

## Data Visualization
The `visualization.py` script provides functions to create various visualizations of the data. This helps in understanding trends and patterns in the dataset.

## Testing
The `testing.ipynb` notebook is used for testing and experimenting with the data. You can use this notebook to try out different analyses and visualizations interactively.
