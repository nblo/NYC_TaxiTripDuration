import pandas as pd 
import numpy as np


def myfunction(df): 
    df['col3'] = df.col1+df.col0
    return df