import pandas as pd 
import numpy as np
import pyproj


def convert_projection_to_utm(df ,col_x_source, col_y_source,
                              col_x_dest ='x_utm', col_y_dest='y_utm',
                              projection_source=pyproj.Proj("+init=EPSG:4326"),
                              projection_dest=pyproj.Proj("+init=EPSG:32618")):
    x, y = pyproj.transform(projection_source,
                            projection_dest,
                            df[col_x_source].values, df[col_y_source].values)
    return df.assign(**{col_x_dest: x, col_y_dest: y})


def calc_distance(df, col_x1_utm, col_x2_utm, col_y1_utm, col_y2_utm,type_='beeline'):
    if type_ =='beeline':
        distance = np.sqrt((df[col_x1_utm]-df[col_x2_utm])**2+(df[col_y1_utm]-df[col_y2_utm])**2)
    elif type_ =='Mannhattan':
        distance = np.abs((df[col_x1_utm]-df[col_x2_utm]))+np.abs((df[col_y1_utm]-df[col_y2_utm]))
    return df.assign(*{f"distance_{type_}": distance})


def calc_cell_id(df, col_x_utm, col_y_utm, col_id='Cell_ID', cell_length=100,keep_coordinates_center=True):
    """     This function calculated the cell id

    :param df:                      Pandas DataFrame, dataframe to append cell id to
    :param col_x_utm:
    :param col_y_utm:
    :param col_id:
    :param cell_length:
    :param keep_coordinates_center:
    :return:
    """
    df[f"x_sw_utm_{col_id}"] = ((df[col_x_utm].values//cell_length)*cell_length).astype(int)
    df[f"y_sw_utm_{col_id}"] = ((df[col_y_utm].values//cell_length)*cell_length).astype(int)
    df[col_id] = f"{cell_length}mN"+(df[f"x_sw_utm_{col_id}"]//cell_length).astype(str)+"E"+(df[f"y_sw_utm_{col_id}"]//cell_length).astype(str)
    if not keep_coordinates_center:
        df.drop(columns=[f"x_sw_utm_{col_id}",f"y_sw_utm_{col_id}"],inplace=True)
    return df
