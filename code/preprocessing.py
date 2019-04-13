import pandas as pd 
import numpy as np
import pyproj


def convert_projection_to_utm(df ,col_x_source, col_y_source,
                              col_x_dest ='x_utm', col_y_dest='y_utm',
                              projection_source=pyproj.Proj("+init=EPSG:4326"),
                              projection_dest=pyproj.Proj("+init=EPSG:32618")):
    x, y = pyproj.transform(projection_source, projection_dest,df[col_x_source].values,df[col_y_source].values)
    return df.assign(**{col_x_dest: x, col_y_dest: y})


def calc_distance(df, col_x1_utm, col_x2_utm, col_y1_utm, col_y2_utm,type_='beeline'):
    if type_ =='beeline':
        distance = np.sqrt((df[col_x1_utm]-df[col_x2_utm])**2+(df[col_y1_utm]-df[col_y2_utm])**2)
    elif type_ =='Mannhattan':
        distance = np.abs((df[col_x1_utm]-df[col_x2_utm]))+np.abs((df[col_y1_utm]-df[col_y2_utm]))
    return df.assign(*{f"distance_{type_}": distance})

