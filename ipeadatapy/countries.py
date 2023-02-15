import pandas as pd
from .api_call import api_call

def countries(country_id=None, keyword=None):
    """Returns all Ipeadata available countries and country IDs."""
#   api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Paises" # DEPRECATED. 
    api = "http://ipeadata.gov.br/api/odata4/Paises"
    call = api_call(api)
    
    cReturn = call[['PAICODIGO','PAINOME']].rename(index=str, columns={"PAICODIGO": "ID", "PAINOME": "COUNTRY"})
    if country_id is not None:
        cReturn = cReturn.loc[cReturn["ID"] == country_id]
    if keyword is not None:
        cReturn = cReturn[cReturn['COUNTRY'].str.contains(keyword)]
    return cReturn
