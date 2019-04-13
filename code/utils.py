"""This module contains miscellaneous utily functions """
import re

def get_cols_by_regex(df, expression):
    """
    Function retrieves all columns of the dataframe that match the regular expression

    :param df:              pandas dataframe to search in
    :param expression:      regex or string to match columns
    :return:                list of matched columns
    """
    regex = re.compile(expression)
    return list(filter(regex.search, df.columns))
