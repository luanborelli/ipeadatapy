import pandas as pd
from .metadata import metadata

def latest_updates():
    """Returns the latest time series' updates from Ipeadata, from the most to the less recent updated time series."""
    df_latest_updates = metadata().sort_values(by='LAST UPDATE', ascending=False)[['CODE', 'NAME','LAST UPDATE']]#.rename(index=str, columns={"SERCODIGO": "CODE", "SERNOME": "NAME", "SERATUALIZACAO": "LAST UPDATE"})
    #num_of_updated_series = list(df_latest_updates['LAST UPDATE'].str.contains('2019-03-22')).count(True)
    #print('Number of series updated today:')
    #print(num_of_updated_series)
    return df_latest_updates 
