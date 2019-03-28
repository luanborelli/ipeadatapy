import pandas as pd
from .api_call import api_call

def countries():
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Paises"
    return api_call(api)[['PAICODIGO','PAINOME']].rename(index=str, columns={"PAICODIGO": "ID", "PAINOME": "COUNTRY"})
