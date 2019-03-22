import requests as req
import pandas as pd

def basic_api_call(api):
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
    return basic_api_call(api).rename(index=str, columns={"FNTID": "ID", "FNTSIGLA": "SIGLA"})['SIGLA']

def metadata(series=None):
    url_final = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/v1/Metadados%s" % url_final
    return basic_api_call(api)

def metadata_odata4(series=None):
    pos_fix = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix
    return basic_api_call(api)

def list_series(keyword=None):
    if keyword is not None:
        df = metadata_odata4()[['SERCODIGO','SERNOME']].rename(index=str, columns={"SERCODIGO": "Código", "SERNOME": "Nome da série"})
        df_f = df[df['Nome da série'].str.contains(keyword)]
    else:
        df_f = metadata_odata4()[['SERCODIGO','SERNOME']].rename(index=str, columns={"SERCODIGO": "Código", "SERNOME": "Nome da série"})
    return df_f

def nivel_region(serie):
    api = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/Metadados('{}')"
           "/Valores?$apply=groupby((NIVNOME))&$orderby=NIVNOME").format(serie)
    return basic_api_call(api)

def describe(series):
    if not list(metadata_odata4(series)['SERNOME'])[0]:
        print("Nome da série: -")
    else:    
        print("Nome da série: "+ list(metadata_odata4(series)['SERNOME'])[0])

    print("Código: "+ series)
    
    if not list(metadata(series)['BASNOME'])[0]:
        print("Grande tema: -")
    else:
        print("Grande tema: "+ list(metadata(series)['BASNOME'])[0])
    
    if not list(metadata(series)['TEMNOME'])[0]:
        print("Tema: -")
    else:
        print("Tema: "+ list(metadata(series)['TEMNOME'])[0])
    
    if not list(metadata(series)['FNTNOME'])[0]:
        print("Fonte: -")
    else:
        print("Fonte:"+ list(metadata(series)['FNTNOME'])[0])
    
    if not list(metadata(series)['FNTSIGLA'])[0]:
        print("Fonte (sigla): -")
    else:
        print("Fonte (sigla): "+ list(metadata(series)['FNTSIGLA'])[0])
    
    if not list(metadata(series)['SERCOMENTARIO'])[0]:
        print("Comentário: -")
    else:
        print("Comentário: "+ list(metadata(series)['SERCOMENTARIO'])[0])
    
    if not list(metadata(series)['SERATUALIZACAO'])[0]:
        print("Data de Atualização: - ")
    else:
        print("Data de Atualização: "+ list(metadata(series)['SERATUALIZACAO'])[0])
    
    if not list(metadata(series)['PERNOME'])[0]:
        print("Periodicidade: - ")
    else:
        print("Periodicidade: "+ list(metadata(series)['PERNOME'])[0])        
    
    if not list(metadata(series)['UNINOME'])[0]:
        print("Unidade de Medida: - ")
    else:
        print("Medida: "+ list(metadata(series)['UNINOME'])[0])
    
    if not list(metadata(series)['MULNOME'])[0]:
        print("Unidade: 1 ")
    else:
        print("Unidade: "+ list(metadata(series)['MULNOME'])[0])

    if not list(metadata(series)['SERSTATUS'])[0]:
        print("Status da série: -")
    else:
        print("Status da série: "+ list(metadata(series)['SERSTATUS'])[0])

def timeseries(series, groupby=None):
    if groupby is not None:
        df = get_nivel_region(series)
        if df['NIVNOME'].isin([groupby]).any():
            api = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/AnoValors"
                   "(SERCODIGO='{}',NIVNOME='{}')?$top=100&$skip=0&$orderby"
                   "=SERATUALIZACAO&$count=true").format(series, groupby)
            return basic_api_call(api)
        return None
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % series
    
    if list(metadata(series)['BASNOME']) == ['Regional']:
        ts_df = basic_api_call(api).rename(index=str, columns={"SERCODIGO": "CODIGO", "VALDATA": "DATA", "VALVALOR": "VALOR ("+list(metadata(series)['UNINOME'])[0]+")"})
    else: 
        ts_df = basic_api_call(api)[['ANO','DIA','MES','SERCODIGO','VALDATA','VALVALOR']].rename(index=str, columns={"SERCODIGO": "CODIGO", "VALDATA": "DATA", "VALVALOR": "VALOR ("+list(metadata(series)['UNINOME'])[0]+")"})
        #basic_api_call(api).rename(index=str, columns={"SERCODIGO": "CODIGO", "VALDATA": "DATA", "VALVALOR": "VALOR ("+list(metadata(series)['UNINOME'])[0]+")"})
    return ts_df

def last_updated():  
    df_last_updated = metadata_odata4().sort_values(by='SERATUALIZACAO', ascending=False)[['SERCODIGO', 'SERNOME','SERATUALIZACAO']].rename(index=str, columns={"SERCODIGO": "CODIGO", "SERNOME": "Nome da Série", "SERATUALIZACAO": "Data/Hora de Atualização"})
    num_of_updated_series = list(df_last_updated['Data/Hora de Atualização'].str.contains('2019-03-22')).count(True)
    print('Number of series updated today:')
    print(num_of_updated_series)
    return df_last_updated
