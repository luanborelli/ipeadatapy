import pandas as pd
from .metadata import metadata

def list_series(keyword=None, code=None, name=None):
    """Lists Ipeadata available time series.

    :param keyword: Filtering keyword, defaults to None
    :type keyword: str, optional
    :return: If no keyword is specified, returns a data frame containing all Ipeadata’s time series. Else, returns only the ones that contains the specified keyword in their names.
keyword.
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
