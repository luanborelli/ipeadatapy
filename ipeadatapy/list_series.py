import pandas as pd
from .metadata_odata4 import metadata_odata4

def list_series(keyword=None):
    """Lists Ipeadata available time series.

    :param keyword: Filtering keyword, defaults to None
    :type keyword: str, optional
    :return: If no keyword is specified, returns a data frame containing all Ipeadata’s time series. Else, returns only the ones that contains the specified keyword in their names.
keyword.
    :rtype: pandas.DataFrame
    """
    if keyword is not None:
        df = metadata_odata4()[['CODE','NAME']]
        df_f = df[df['NAME'].str.contains(keyword)]
    else:
        df_f = metadata_odata4()[['CODE','NAME']]
    return df_f
