import pandas as pd
from .api_call import api_call
from .metadata import metadata

def timeseries(series, groupby=None):
    if groupby is not None:
        df = get_nivel_region(series)
        if df['NIVNOME'].isin([groupby]).any():
            api = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/AnoValors"
                   "(SERCODIGO='{}',NIVNOME='{}')?$top=100&$skip=0&$orderby"
                   "=SERATUALIZACAO&$count=true").format(series, groupby)
            return api_call(api)
        return None
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % series
    
    if list(metadata(series)['BIG THEME']) == ['Regional']:
        ts_df = api_call(api).rename(index=str, columns={"SERCODIGO": "CODE", "VALDATA": "DATE", "VALVALOR": "VALUE ("+list(metadata(series)['MEASURE'])[0]+")"})
    else: 
        ts_df = api_call(api)[['ANO','DIA','MES','SERCODIGO','VALDATA','VALVALOR']].rename(index=str, columns={"ANO": "YEAR", "DIA": "DAY", "MES": "MONTH", "SERCODIGO": "CODE", "VALDATA": "DATE", "VALVALOR": "VALUE ("+list(metadata(series)['MEASURE'])[0]+")"})
        #api_call(api).rename(index=str, columns={"SERCODIGO": "CODIGO", "VALDATA": "DATA", "VALVALOR": "VALOR ("+list(metadata(series)['UNINOME'])[0]+")"})
    return ts_df
