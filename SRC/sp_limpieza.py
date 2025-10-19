
import pandas as pd



def minus (df):
    
    """_summary_
    """
    for col in df.select_dtypes (include='O').columns:
        df[col]=df[col].str.lower()


def puntos (df):

    """_summary_
    """
    for col in df.select_dtypes(include='O').columns:
      df[col]=df[col].str.replace('.','_')


def comas_float(df):
    """_summary_
    """
    for col in df.select_dtypes (include='O').columns:                    
        df[col]=df[col].str.replace(',','.')
        try:
            df[col]=df[col].astype('float64')
        except:
            pass 
   
