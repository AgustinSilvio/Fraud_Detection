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

Por favor lea [install.md](install.md) para detalles sobre cómo configurar este proyecto.

# Organización del proyecto

    ├── LICENSE
    ├── tasks.py           <- Invocar con comandos como `notebook`.
    ├── README.md          <- README.
    ├── install.md         <- Instrucciones detalladas para configurar este proyecto.
    ├── data
    │   ├── external       <- Datos de fuentes de terceros.
    │   ├── interim        <- Datos intermedios que han sido transformados.
    │   ├── processed      <- Los conjuntos de datos finales y canónicos para la modelización.
    │   └── raw            <- El volcado de datos original e inmutable.
    │
    ├── models             <- Modelos entrenados, predicciones o resúmenes de modelos
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Diccionarios de datos, manuales y todo otro material explicativo.
    │
    ├── reports            <- Análisis generado como HTML, PDF, LaTeX, etc.
    │   └── figures         <- Gráficos y figuras generados para ser utilizados en informes.
    │
    ├── environment.yml    <- El archivo de requisitos para reproducir el entorno de análisis.
    │
    ├── .here              <- Archivo que detendrá la búsqueda si ninguno de los otros criterios
    │                         se aplica al buscar al jefe del proyecto.
    │
    ├── setup.py           <- Hace que el proyecto sea instalable con pip (pip install -e .)
    │                         así se puede importar mlparadetectarfraudes.
    │
    └── mlparadetectarfraudes               <- Código fuente para usar en este proyecto.
        ├── __init__.py    <- Convierte mlparadetectarfraudes en un módulo de Python.
        │
        ├── data           <- Scripts para descargar o generar datos.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts para convertir datos en bruto en características para modelar.
        │   └── build_features.py
        │
        ├── models         <- Scripts para entrenar modelos y luego usar modelos entrenados para 
        │   │                 hacer predicciones.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts para ayudar con tareas comunes.
            └── paths.py   <- Funciones auxiliares para la referencia de archivos
        │                     relativa a través del proyecto.
        └── visualization  <- Scripts para crear visualizaciones.
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
