import pandas as pd
from .metadata import metadata

def list_series(keyword=None, code=None, name=None):
    """Lists Ipeadata available time series.

    :param keyword: Filtering keyword, defaults to None
    :type keyword: str, optional
    :param code: Specifies a time series code to return. code must be a time series code respecting case sensitiveness
    :type code: str, optional
    :param name: Specifies a time series name to return. name must be a time series name respecting case sensitiveness
    :type name: str, optional
    :return: If no keyword is specified, returns a data frame containing all Ipeadata’s time series. Otherwise, returns a data frame respecting the introduced parameters
    :rtype: pandas.DataFrame
    """
    df = metadata()[['CODE','NAME']]
    if code is not None:
        df = df.loc[df["CODE"] == code]
    if name is not None:
        df = df.loc[df["NAME"] == name]
        
    if keyword is not None:
        df_f = df[df['NAME'].str.contains(keyword)]
    else:
        df_f = df
    return df_f
