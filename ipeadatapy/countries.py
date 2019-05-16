import pandas as pd
from .api_call import api_call

def countries(country_id=None, keyword=None):
    """Returns all Ipeadata available countries and country IDs."""
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Paises"
    cReturn = api_call(api)[['PAICODIGO','PAINOME']].rename(index=str, columns={"PAICODIGO": "ID", "PAINOME": "COUNTRY"})
    if country_id is not None:
        cReturn = cReturn.loc[cReturn["ID"] == country_id]
    if keyword is not None:
        cReturn = cReturn[cReturn['COUNTRY'].str.contains(keyword)]
    return cReturn
