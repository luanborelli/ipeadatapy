import pandas as pd
from .metadata_odata4 import metadata_odata4

def list_series(keyword=None):
    if keyword is not None:
        df = metadata_odata4()[['CODE','NAME']]
        df_f = df[df['NAME'].str.contains(keyword)]
    else:
        df_f = metadata_odata4()[['CODE','NAME']]
    return df_f
