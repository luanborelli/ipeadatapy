import pandas as pd
from .api_call import api_call

def territories(name=None, level=None, territory_id=None, area=None, areaGreaterThan=None, areaSmallerThan=None, capital=None):
    """
    :param name: Territory name by which the return will be fitered.
    :type name: str, optional
    :param level: Territory name by which the return will be fitered.
    :type level: str, optional
    :param territory_id: Territory ID by which the return will be fitered.
    :type territory_id: str, optional
    :param area: Territorial area by which the return will be fitered.
    :type area: float, optional 
    :param areaGreaterThan: Territorial area restriction by which the return will be fitered. The function will return only territories with area strictly greater than the submitted value.
    :type areaGreaterThan: float, optional
    :param areaSmallerThan: Territorial area restriction by which the return will be fitered. The function will return only territories with area strictly smaller than the submitted value.
    :type areaSmallerThan: float, optional
    :param capital: Return only capitals? True or False.
    :type capital: bool, optional
    :return: Returns available Ipeadata territories.
    :rtype: pandas.DataFrame
    """
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
