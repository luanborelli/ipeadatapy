import requests as req
import pandas as pd

def api_call(api):
    response = req.get(api)
    if response.status_code == req.codes.ok:
        json_response = response.json()
        if 'value' in json_response:
            try:
                data_frame = pd.DataFrame(json_response['value'])
                return data_frame
            except Exception:
                return None
    return None
   
def sources():
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Fontes"
    return api_call(api).rename(index=str, columns={"FNTID": "ID", "FNTSIGLA": "SIGLA"})['SIGLA']

def metadata(series=None):
    url_final = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/v1/Metadados%s" % url_final
    return api_call(api).rename(index=str, columns={"TEMNOME": "THEME", "BASNOME": "BIG THEME", "FNTNOME": "SOURCE", "FNTSIGLA": "SOURCE ACRONYM", "FNTURL": "SOURCE URL", "MULNOME": "UNIT", "PAICODIGO": "COUNTRY", "PERNOME": "FREQUENCY", "SERATUALIZACAO": "LAST UPDATE", "SERCODIGO": "CODE", "SERCOMENTARIO": "COMMENT", "SERNOME": "NAME", "SERNUMERICA": "NUMERICA", "SERSTATUS": "SERIES STATUS", "TEMCODIGO": "THEME CODE", "UNINOME": "MEASURE"})

def metadata_odata4(series=None):
    pos_fix = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix
    return api_call(api).rename(index=str, columns={"TEMNOME": "THEME", "BASNOME": "BIG THEME", "FNTNOME": "SOURCE", "FNTSIGLA": "SOURCE ACRONYM", "FNTURL": "SOURCE URL", "MULNOME": "UNIT", "PAICODIGO": "COUNTRY", "PERNOME": "FREQUENCY", "SERATUALIZACAO": "LAST UPDATE", "SERCODIGO": "CODE", "SERCOMENTARIO": "COMMENT", "SERNOME": "NAME", "SERNUMERICA": "NUMERICA", "SERSTATUS": "SERIES STATUS", "TEMCODIGO": "THEME CODE", "UNINOME": "MEASURE"})

def list_series(keyword=None):
    if keyword is not None:
        df = metadata_odata4()[['CODE','NAME']]
        df_f = df[df['NAME'].str.contains(keyword)]
    else:
        df_f = metadata_odata4()[['CODE','NAME']]
    return df_f

#def nivel_region(serie):
#    api = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/Metadados('{}')"
#           "/Valores?$apply=groupby((NIVNOME))&$orderby=NIVNOME").format(serie)
#    return api_call(api)

def describe(series):
    if not list(metadata_odata4(series)['NAME'])[0]:
        print("Timeseries' name: -")
    else:    
        print("Timeseries' name: "+ list(metadata_odata4(series)['NAME'])[0])

    print("Code: "+ series)
    
    if not list(metadata(series)['BIG THEME'])[0]:
        print("Big theme: -")
    else:
        print("Big theme: "+ list(metadata(series)['BIG THEME'])[0])
    
    if not list(metadata(series)['THEME'])[0]:
        print("Theme: -")
    else:
        print("Theme: "+ list(metadata(series)['THEME'])[0])
    
    if not list(metadata(series)['SOURCE'])[0]:
        print("Source: -")
    else:
        print("Source:"+ list(metadata(series)['SOURCE'])[0])
    
    if not list(metadata(series)['SOURCE ACRONYM'])[0]:
        print("Source acronym: -")
    else:
        print("Source acronym: "+ list(metadata(series)['SOURCE ACRONYM'])[0])
    
    if not list(metadata(series)['COMMENT'])[0]:
        print("Comment: -")
    else:
        print("Comment: "+ list(metadata(series)['COMMENT'])[0])
    
    if not list(metadata(series)['LAST UPDATE'])[0]:
        print("Last update date: - ")
    else:
        print("Last update date: "+ list(metadata(series)['LAST UPDATE'])[0])
    
    if not list(metadata(series)['FREQUENCY'])[0]:
        print("Frequency: - ")
    else:
        print("Frequency: "+ list(metadata(series)['FREQUENCY'])[0])        
    
    if not list(metadata(series)['MEASURE'])[0]:
        print("Measure: - ")
    else:
        print("Measure: "+ list(metadata(series)['MEASURE'])[0])
    
    if not list(metadata(series)['UNIT'])[0]:
        print("Unit: 1 ")
    else:
        print("Unit: "+ list(metadata(series)['UNIT'])[0])

    if not list(metadata(series)['SERIES STATUS'])[0]:
        print("Timeseries' status: -")
    else:
        print("Timeseries' status: "+ list(metadata(series)['SERIES STATUS'])[0])

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

def last_updated():  
    df_last_updated = metadata_odata4().sort_values(by='LAST UPDATE', ascending=False)[['CODE', 'NAME','LAST UPDATE']]#.rename(index=str, columns={"SERCODIGO": "CODE", "SERNOME": "NAME", "SERATUALIZACAO": "LAST UPDATE"})
    num_of_updated_series = list(df_last_updated['LAST UPDATE'].str.contains('2019-03-22')).count(True)
    print('Number of series updated today:')
    print(num_of_updated_series)
    return df_last_updated   
