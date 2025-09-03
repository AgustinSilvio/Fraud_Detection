**Contacto**: agustinsilviorojas@outlook.com.ar



**Linkedin:**

<a href="https://www.linkedin.com/in/agustinsilviorojas/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;




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
