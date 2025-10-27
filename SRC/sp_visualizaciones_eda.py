import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def matriz_correlacion(df):

    #calcular matriz de correlacion
    corr_matrix = df.corr(numeric_only=True)
    #crear la figura
    plt.figure(figsize=corr_matrix.shape)

    # crear una mascara para mostrar solo la parte triangular
    mask = np.triu(np.ones_like(corr_matrix,dtype=bool))

    #Graficar el mapa de calor
    sns.heatmap(corr_matrix,annot=True,vmin=-1,vmax=1,cmap='cool', mask=mask)
    plt.show()



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


def mapa(df,lat, lon, valores):
    fig = px.scatter_mapbox(df, lat= lat, lon = lon, size = valores,
                            zoom = 1, mapbox_style = 'open-street-map')
    fig.show()  