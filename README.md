**Contacto**: agustinsilviorojas@outlook.com.ar


**Social media:**

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAdCAMAAACKeiw+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAFuUExURf3+/4u34ix7yzB+yzF+zMvf8gJhwABgvwVjwbrU7gJhvwdkwQpmwgRiwAllwr3W7wBfvw9pwxlvxgZjwQtmwgJgv02Q08LZ8Nbl9YOy4AxnwwNhwCx8y+/1+////22k2gBdvwBev12a16XG6AFgwAhkwTWBzfn7/nap3QBdvglmwmef2ePu+Ovy+pvA5hNrxAhlwhpwxiN2yABavQBZvQpnwhFrxGuj2nOn3HKn3C17ygRhwGGd2HOo3B5zx1CS03+v34a04WCc1yJ1yANiwBxyxvz9/mGc1wBYvRhuxWOe2KfI6eHs91aV1RtxxlyZ1hduxdjn9fv8/vH2/DeCzQFfv/P4/Pv9/pvB5gNfv4i14h1xxjaBzdfm9dLj9LDN6wBcvgBVu3Gn3BlwxliX1e70+wJiwGOd2Bhvxeny+XWp3ABbvgZkwRNsxIWz4Y244wVfvxFqxHir3T+HzwViwAVhwISy4Qtnwoq34gAAAN7JZ5kAAAB6dFJOU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A6D/oJgAAAAlwSFlzAAAXEQAAFxEByibzPwAAAVJJREFUOE99U7FugzAQzQASekvEXjGz0MELS4d+QMYIdWpkgZQpiqwufH7euzMkaUnvsI+753eHz2bXXEPxQsK12ZVAhWpTgHK3d2xzRdwLThVSkvmt1d6T/5SHOeEJ4VPB2CgaSh8ZYBINLuXiDMdJ8IkllECza4arY2Y/QKb88pIwpkP3/hg3XZLTphCt6rMarCKRqAy4D00MLjC5bdv2b0g9bcD0OU/BcnltjP5p44FmOsnppnttjIPiDmtQhoJt8NpIDqdvR2z+WveN8MBu5lRYFjVbtVd2LfYpxtjTDiPhv+wesCZ3bD1hY3f0P+JF7J5RwQP3tsWODpPttwWoHV7YlvwVOyfP7LX2P2y6zTlelKRl7bP8O7ueKUegNZNQyGfP803lefJEUcvqKN0nLphhJaqpaqTdBDe5LYzyeCi6qFzBd5tYW//YcUMYDNfmBsjyiwsq+7iKAAAAAElFTkSuQmCC)[LinkedIn](https://www.linkedin.com/in/agust%C3%ADnsilviorojas/)

# Índice

- [Índice](#índice)
- [Instroducción](#instroducción)
- [Guía de instalación](#guía-de-instalación)
- [Organización del proyecto](#organización-del-proyecto)
  - [Notebooks](#notebooks)

# Instroducción
Tecnicas de machine learning para detectar fraudes. Ejercicio teórico.
Proceso de aprobación:

1-Cliente solicita crédito desde la app

2-ML analiza: historial interno o datos alternativos

3-Decisión instantanea: Probabilidad de impago

Por ejemplo: si un usuario recarga su saldo frecuentemente y gasta en comercios estables tiene menor riesgo. Transacciones altas en horarios atípicos sería más riesgoso.
  
# Guía de instalación

Por favor lea [install.md](install.md) for details on how to set up this project.

# Organización del proyecto

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so mlparadetectarfraudes can be imported.
    │
    └── mlparadetectarfraudes               <- Source code for use in this project.
        ├── __init__.py    <- Makes mlparadetectarfraudes a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---


## Notebooks

- [00-before-to-start.ipynb](notebooks/00-before-to-start.ipynb): Guía inicial para preparar el entorno y configurar el proyecto.
- [01-EDA.ipynb](notebooks/01-EDA.ipynb): Análisis exploratorio de datos y visualización de patrones de fraude.
- [02-Preparation.ipynb](notebooks/02-Preparation.ipynb): Preparación de los datos.
- [03-PCA.ipynb](notebooks/03-PCA.ipynb): PCA.
- [04-RadomForest.ipynb](notebooks/04-RadomForest.ipynb): Entrenamiento y evaluación de modelos Random Forest para detección de fraude.
- [05-XGBoost.ipynb](notebooks/05-XGBoost.ipynb): Entrenamiento y evaluación de modelos XGBoost para detección de fraude.
- [06-Comparación.ipynb](notebooks/06-Comparación.ipynb): Comparación de los resultados de los modelos Random Forest y XGBoost