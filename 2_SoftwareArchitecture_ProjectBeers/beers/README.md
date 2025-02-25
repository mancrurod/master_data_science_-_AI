# Proyecto de análisis de cervezas

(Test project)

Este proyecto tiene como objetivo analizar y visualizar datos de diferentes cervezas y sus características. Utilizamos un conjunto de datos que contiene información sobre varias cervezas, incluyendo su estilo, contenido de alcohol (ABV), amargor (IBU), y más.

## Estructura del proyecto

- **data/**: Contiene el archivo `beers.csv` con los datos de las cervezas.
- **src/**: Contiene los scripts de Python para la transformación, exploración y visualización de los datos.
  - `transformation.py`: Script para transformar y limpiar los datos.
  - `exploration.py`: Script para explorar los datos y realizar análisis descriptivos.
  - `visualization.py`: Script para generar visualizaciones de los datos.
- **main.py**: Script principal para ejecutar el análisis completo.
- **testing.ipynb**: Notebook de Jupyter para pruebas y desarrollo interactivo.

## Requisitos

- Python 3.8 o superior
- Bibliotecas de Python: pandas, matplotlib, seaborn, numpy

## Cómo ejecutar

1. Clonar el repositorio.
2. Instalar las dependencias necesarias:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```
3. Ejecutar el script principal:
   ```bash
   python main.py
   ```