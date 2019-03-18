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

def metadata(serie=None):
    url_final = "('%s')" % serie if serie is not None else ""
    api = "http://www.ipeadata.gov.br/api/v1/Metadados%s" % url_final
    return basic_api_call(api)

def metadata_odata4(series=None):
    pos_fix = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix
    return basic_api_call(api)

def list_series(series=None):
    if series is not None:
        df = metadata_odata4()[['SERCODIGO','SERNOME']].rename(index=str, columns={"SERCODIGO": "Código", "SERNOME": "Nome da série"})
        df_f = df.loc[df['Nome da série'] == series]
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

def dataseries(serie, groupby=None):
    if groupby is not None:
        df = get_nivel_region(serie)
        if df['NIVNOME'].isin([groupby]).any():
            api = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/AnoValors"
                   "(SERCODIGO='{}',NIVNOME='{}')?$top=100&$skip=0&$orderby"
                   "=SERATUALIZACAO&$count=true").format(serie, groupby)
            return basic_api_call(api)
        return None
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % serie
    return basic_api_call(api).rename(index=str, columns={"SERCODIGO": "CODIGO", "VALDATA": "DATA", "VALVALOR": "VALOR ("+list(metadata(serie)['UNINOME'])[0]+")"})
