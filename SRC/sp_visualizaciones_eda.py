#tratamiento de datos
import pandas as pd
import numpy as np

#visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def matriz_correlacion(df):
    """
    Qué realiza la función  
        Calcula y visualiza la matriz de correlación entre las columnas numéricas del DataFrame.  
      
    Qué incluye el análisis  
        - Calcula la correlación de Pearson entre todas las columnas numéricas.  
        - Genera un gráfico de mapa de calor (heatmap) usando seaborn.  
        - Muestra solo la mitad superior de la matriz para mayor claridad.  
        - Los valores se anotan y se colorean según la intensidad de correlación (-1 a 1).  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se calculará la matriz de correlación.

    Returns:
    None
    """
    #calcular matriz de correlacion
    corr_matrix = df.corr(numeric_only=True)
    #crear la figura
    plt.figure(figsize=corr_matrix.shape)

    # crear una mascara para mostrar solo la parte triangular
    mask = np.triu(np.ones_like(corr_matrix,dtype=bool))

    #Graficar el mapa de calor
    sns.heatmap(corr_matrix,annot=True,vmin=-1,vmax=1,cmap='cool', mask=mask)
    plt.show()



def subplot_col_cat(df):
    """
    Qué realiza la función  
        Genera gráficos de barras para todas las columnas categóricas del DataFrame, mostrando la distribución de cada categoría.  
      
    Qué incluye el análisis  
        - Identifica todas las columnas de tipo object o category.  
        - Crea un subplot con 3 gráficos por fila y filas suficientes según el número de columnas.  
        - Grafica la frecuencia de cada categoría usando seaborn countplot.  
        - Añade títulos, etiquetas y rotación de ejes para mejorar la legibilidad.  
        - Elimina subplots sobrantes si hay menos columnas que subplots generados.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se generarán los gráficos.

    Returns:
    None
    """
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
        sns.countplot(data = df, x=col, ax=axes[i], hue=col, palette="rocket",legend=False)
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

        


def subplot_col_num(df):
    """
    Qué realiza la función:
        - Identifica todas las columnas numéricas del DataFrame.
        - Para cada columna, genera:
            1. Un histograma con 200 bins mostrando la distribución de los valores.
            2. Un boxplot para visualizar posibles outliers.
        - Cada columna utiliza un color distinto de la paleta 'rocket' para mantener consistencia visual.
        - Ajusta automáticamente el tamaño de la figura según el número de columnas.
        - Elimina ejes sobrantes si hay más subplots que columnas.

    Parámetros:
        df (pd.DataFrame): DataFrame sobre el que se generarán los gráficos.

    Retorna:
        None: La función muestra los gráficos directamente y no devuelve valores.

    Uso:
        subplot_col_num(df_no_nulos)
    """


    col_nums = df.select_dtypes(include='number').columns
    num_graph = len(col_nums)

    # Extraer colores de la paleta rocket
    rocket_colors = sns.color_palette('rocket', num_graph)

    num_rows = (num_graph + 2) // 2
    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows * 5))

    for i, col in enumerate(col_nums):
        color = rocket_colors[i]  # color de la columna i

        # Histograma con color
        sns.histplot(data=df, x=col, ax=axes[i,0], bins=200, color=color)
        axes[i,0].set_title(f'Distribucion de {col}')
        axes[i,0].set_xlabel(col)
        axes[i,0].set_ylabel('Frecuencia')
        
        # Boxplot con color
        sns.boxplot(data=df, x=col, ax=axes[i,1], color=color)
        axes[i,1].set_title(f'Boxplot de {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    



def mapa(df,lat, lon, valores):
    """
    Qué realiza la función  
        Crea un mapa interactivo de puntos utilizando coordenadas geográficas, mostrando la intensidad o tamaño de un valor asociado a cada punto.  
      
    Qué incluye la visualización  
        - Utiliza Plotly Express para generar un scatter_mapbox.  
        - Cada punto se coloca según latitud y longitud.  
        - El tamaño de los puntos refleja los valores de la columna especificada.  
        - Configura el zoom inicial y el estilo del mapa.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene las coordenadas y valores a graficar.
    lat (str): Nombre de la columna de latitud.
    lon (str): Nombre de la columna de longitud.
    valores (str): Nombre de la columna cuyos valores determinarán el tamaño de los puntos.

    Returns:
    None
    """
    fig = px.scatter_mapbox(df, lat= lat, lon = lon, size = valores,
                            zoom = 1, mapbox_style = 'open-street-map')
    fig.show()  




def conversion_categorica(df, variables_relevantes, target='subscription_prod'):
    """
    Calcula y visualiza la tasa de conversión (%) de un target por categorías de variables.

    Parámetros:
        df (pd.DataFrame): DataFrame que contiene las variables.
        variables_relevantes (list): Lista de columnas categóricas a analizar.
        target (str): Columna objetivo (por defecto 'subscription_prod').

    Muestra:
        - Impresion en consola de la tasa de conversión por categoría.
        - Gráficos de barras con la paleta 'rocket' para cada variable.
    """
    for col in variables_relevantes:
        # Calcular tasa de conversión por categoría
        tasa = df.groupby(col)[target].apply(
            lambda x: (x == 'yes').sum() / len(x) * 100
        ).sort_values(ascending=False)
        
        print(f"--------------------------------")
        print(f"TASA DE CONVERSIÓN POR {col.upper()}")
        print(f"--------------------------------")
        print(tasa.round(2))
        
        # Gráfico
        num_cats = df[col].nunique()
        fig_width = max(6, num_cats * 1.2)
        plt.figure(figsize=(fig_width, 5))
        
        # Barplot con hue = categoría para aplicar la paleta rocket
        sns.barplot(
            x=tasa.index,
            y=tasa.values,
            hue=tasa.index,
            dodge=False,
            palette='rocket',
            legend=False
        )
        
        plt.title(f'Tasa de Conversión (%) por {col}')
        plt.ylabel('% de Aceptación')
        plt.xlabel(col)
        plt.xticks(rotation=45, ha='right')
        
        # Añadir valores encima de las barras
        for i, v in enumerate(tasa):
            plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        plt.show()





