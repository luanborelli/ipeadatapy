import pandas as pd
from .api_call import api_call

def themes(theme_id=None, name=None, macro=None, regional=None, social=None):
    """
    :param theme_id: Theme ID by which the return will be filtered
    :type theme_id: int, optional
    :param name: Theme name by which the return will be filtered
    :type name: str, optional
    :param macro: If macro=1, the function will return only themes related to the Macroeconomics big theme
    :type macro: int, optional
    :param regional: If regional=1, the function will return only themes related to the Regional big theme
    :type regional: int, optional
    :param social: If social=1, the function will return only themes related to the Social big theme
    :type social: int, optional
    :return: Returns available Ipeadata themes
    :rtype: pandas.DataFrame
    """
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
