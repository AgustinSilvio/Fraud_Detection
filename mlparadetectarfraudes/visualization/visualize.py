import numpy as np
import pandas as pd
from scipy.stats import pointbiserialr, chi2_contingency

def calculate_correlations(df : pd.DataFrame, target_col='is_fraud'):
    """
La función calculate_correlations calcula:

Para variables numéricas: Correlación punto-biserial con la variable objetivo binaria

Para variables categóricas: V de Cramér, que mide la asociación entre dos variables categóricas

Esta función es útil para entender qué variables están más correlacionadas con la variable objetivo en un dataset con variables mixtas (numéricas y categóricas).
    """
    correlations = {}
    
    # Para variables numéricas: correlación punto-biserial
    numerical_features = df.select_dtypes(include=[np.number]).columns
    numerical_features = [f for f in numerical_features if f != target_col]
    
    for feature in numerical_features:
        corr, _ = pointbiserialr(df[feature], df[target_col])
        correlations[feature] = corr
    
    # Para variables categóricas: V de Cramér
    categorical_features = df.select_dtypes(include=['object', 'category']).columns
    
    def cramers_v(x, y):
        confusion_matrix = pd.crosstab(x, y)
        chi2 = chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2 / n
        r, k = confusion_matrix.shape
        phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
        rcorr = r - ((r-1)**2)/(n-1)
        kcorr = k - ((k-1)**2)/(n-1)
        return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))
    
    for feature in categorical_features:
        correlations[feature] = cramers_v(df[feature], df[target_col])
    
    return pd.Series(correlations).sort_values(ascending=False)
