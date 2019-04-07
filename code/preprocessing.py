import pandas as pd 



def myfunction(df): 
    df['col3'] = df.col1+df.col0
    return df