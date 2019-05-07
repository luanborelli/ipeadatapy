import pandas as pd
from .api_call import api_call

def themes(theme_id=None, name=None, macro=None, regional=None, social=None):
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Temas"
    thReturn = api_call(api)[['TEMCODIGO','TEMNOME','MACRO','REGIONAL','SOCIAL']].rename(index=str, columns={"TEMCODIGO": "ID", "TEMNOME": "NAME"})
    if theme_id is not None:
        thReturn = thReturn.loc[thReturn["ID"] == theme_id]
    if name is not None:
        thReturn = thReturn.loc[thReturn["NAME"] == name]
    if macro is not None:
        thReturn = thReturn.loc[thReturn["MACRO"] == macro]
    if regional is not None:
        thReturn = thReturn.loc[thReturn["REGIONAL"] == regional]
    if social is not None:
        thReturn = thReturn.loc[thReturn["SOCIAL"] == social]
    return thReturn
