import pandas as pd
from .api_call import api_call

def themes():
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Temas"
    return api_call(api)[['TEMCODIGO','TEMNOME','MACRO','REGIONAL','SOCIAL']].rename(index=str, columns={"TEMCODIGO": "ID", "TEMNOME": "NOME"})
