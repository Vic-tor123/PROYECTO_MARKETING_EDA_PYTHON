import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.experimental import enable_iterative_imputer #instalar antes de importar ver en google pypi sklearn
from sklearn.impute import KNNImputer, IterativeImputer




def estadist_col_cat (df):   

    for col in df.select_dtypes(include='O').columns:
        print (col.upper())
        print (df[col].value_counts()/df.shape[0]*100)
        print('------------------------')         



    # calculo numerico de los outliers

def calculo_outliers (df, cols):
    for col in cols:
        q_75 = df[col].quantile(0.75)
        q_25 = df[col].quantile(0.25)
        rango_itq = q_75 - q_25
        inferior = q_25 - (rango_itq*1.5)
        superior = q_75 + (rango_itq*1.5) 
        outliers = df[(df[col]<inferior) | (df[col]>superior)]
        num_outliers = len(outliers)

        per_outliers = num_outliers/df.shape[0]*100
        print(f'En la columna {col.upper()} tenenemos un total de {num_outliers} outliers, lo que representa un {per_outliers}% del total') 




    # Imputacion de nulos con ITERATIVE (estadisticos avanzados)

def imputar_iterative(df, lista_columnas):
    iter_imputer = IterativeImputer (max_iter=50,random_state=42)
    data_imputed = iter_imputer.fit_transform(df[lista_columnas])
    new_col = [col +"_iterative" for col in lista_columnas]
    df[new_col]= data_imputed
    display(df[new_col].describe().T)
    return df      


    # Imputacion de nulos con knn (estadisticos avanzados)

def imputar_knn(df, lista_columnas):
    knn_imputer = KNNImputer (n_neighbors=5)
    data_imputed = knn_imputer.fit_transform(df[lista_columnas])
    new_col = [col +"_knn" for col in lista_columnas]
    df[new_col]= data_imputed
    return df



