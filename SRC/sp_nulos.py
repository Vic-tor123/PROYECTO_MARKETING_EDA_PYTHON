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


# visulalizacion columnas categoricas (si le pasamos df_nulos nos dara la visualizacion para df con columnas con nulos)

def subplot_col_cat(df):
    #seleccionar columas categoricas
    categorical_cols = df.select_dtypes(include=['object','category']).columns
    if len(categorical_cols)==0:
        print("No hay columnas categoricas en el DataFrame.")
        return
    
    # configurar el tamaño de la figura
    num_cols = len(categorical_cols)
    rows = (num_cols + 2) // 3 # Calcular filas necesarias para 3 columnas por fila
    fig,axes = plt.subplots(rows, 3, figsize = (15, rows *5))
    axes = axes.flatten() # Convertir los ejes a un array de una 1d plano para facil iteracion

    #generar fraficos para cada columna categorica
    for i, col in enumerate(categorical_cols):
        sns.countplot(data = df, x=col, ax=axes[i], hue=col, palette="GnBu",legend=False)
        axes[i].set_title(f'Distribucion de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90) #Rotar etiquetas si es necesario
 
    # Eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(i +1, len (axes)):
        fig.delaxes(axes[j])

    #Ajustar disenho
    plt.tight_layout()
    plt.show()





        # Columnas numericas, visualizacion de outliers, SUBPLOTS

def subplot_col_num(df):

    col_nums=df.select_dtypes(include='number').columns
    num_graph = len(col_nums)

    num_rows = (num_graph+2)//2

    fig, axes = plt.subplots(num_graph,2, figsize = (15, num_rows*5))

    for i, col in enumerate(col_nums):

        sns.histplot(data = df, x=col, ax=axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribucion de {col}')
        axes[i,0].set_xlabel(col)
        axes[i,0].set_ylabel('Frecuencia')
        
        sns.boxplot(data=df, x=col, ax = axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')

    for j in range(i +1, len (axes)):
        fig.delaxes(axes[j])

    #Ajustar disenho
    plt.tight_layout()
    plt.show()


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