import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





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