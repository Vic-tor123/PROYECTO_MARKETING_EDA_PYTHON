#tratamiento de datos
import pandas as pd



def minus (df):
    
    """
    Qué realiza la función  
        Convierte todos los valores de texto (tipo object) en el DataFrame a minúsculas.  
      
    Qué incluye la transformación  
        - Recorre todas las columnas de tipo texto.  
        - Aplica el método .str.lower() a cada una para uniformar el formato de texto.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la transformación.

    Returns:
    None
    """

    for col in df.select_dtypes (include='O').columns:
        df[col]=df[col].str.lower()


def puntos (df):

    """
    Qué realiza la función  
        Reemplaza los puntos ('.') por guiones bajos ('_') en todas las columnas de texto del DataFrame.
      
    Qué incluye la transformación  
        - Recorre las columnas de tipo texto (object).  
        - Sustituye los puntos por guiones bajos para estandarizar nombres o valores.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la transformación.

    Returns:
    None
    """

    for col in df.select_dtypes(include='O').columns:
      df[col]=df[col].str.replace('.','_')


def comas_float(df):
    """
    Qué realiza la función  
        Convierte valores numéricos escritos como texto con comas como separador decimal a tipo float.  
      
    Qué incluye la transformación  
        - Recorre todas las columnas de tipo texto (object).  
        - Reemplaza las comas (',') por puntos ('.') para normalizar el formato decimal.  
        - Intenta convertir cada columna a tipo float64; si no es posible, se mantiene el valor original.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la transformación.

    Returns:
    None
    """
    for col in df.select_dtypes (include='O').columns:                    
        df[col]=df[col].str.replace(',','.')
        try:
            df[col]=df[col].astype('float64')
        except:
            pass 
   
