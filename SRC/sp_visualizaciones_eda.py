import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



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