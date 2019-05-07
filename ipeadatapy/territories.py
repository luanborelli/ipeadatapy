import pandas as pd
from .api_call import api_call

def territories(name=None, level=None, territory_id=None, area=None, areaGreaterThan=None, areaSmallerThan=None, capital=None):
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Territorios"
    tReturn = api_call(api)[['TERNOME', 'TERCODIGO', 'NIVNOME', 'TERAREA','TERCAPITAL']].rename(index=str, columns={"TERNOME": "NAME", "TERCODIGO": "ID","NIVNOME": "LEVEL","TERAREA": "AREA", "TERCAPITAL": "CAPITAL"})
    if name is not None:
        tReturn = tReturn.loc[tReturn["NAME"] == name]
    if level is not None:
        tReturn = tReturn.loc[tReturn["LEVEL"] == level]
    if territory_id is not None:
        tReturn = tReturn.loc[tReturn["ID"] == territory_id]
    if area is not None:
        tReturn = tReturn.loc[tReturn["AREA"] == area]
    if areaGreaterThan is not None:
        tReturn = tReturn.loc[tReturn["AREA"] > areaGreaterThan]
    if areaSmallerThan is not None:
        tReturn = tReturn.loc[tReturn["AREA"] < areaSmallerThan]
    if capital is not None:
        tReturn = tReturn.loc[tReturn["CAPITAL"] == capital]
    return tReturn
