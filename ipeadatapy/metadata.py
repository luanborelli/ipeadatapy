import pandas as pd
from .api_call import api_call

def metadata(series=None, big_theme=None, source=None, country=None, frequency=None, unit=None, measure=None, status=None, source_ext=None, source_url=None, last_update=None, code=None, comment=None, name=None, numerica=None, theme_id=None):
    """
    :param series: Time series code.
    :type series: str, optional
    :param big_theme: Big theme by which the return will be fitered. Options: "Macroeconômico", "Regional" or "Social"
    :type big_theme: str, optional
    :param source: Source by which the return will be filtered. For available sources run sources() function.
    :type source: str, optional
    :param country: Country ID by which the return will be filtered. For available countries and their IDs run countries() function.
    :type country: str, optional
    :param frequency: Frequency by which the return will be filtered.
    :type frequency: str, optional
    :param unit: Unit by which the return will be filtered.
    :type unit: str, optional
    :param measure: Measure by which the return will be filtered.
    :type measure: str, optional
    :param status: Status by which the return will be filtered. Available options: "A" and "I"
    :type status: str, optional
    :param source_ext: Source extended name by which the return will be filtered.
    :type source_ext: str, optional
    :param source_url: Source URL by which the return will be filtered.
    :type source_url: str, optional
    :param last_update: Last update date by which the return will be filtered.
    :type last_update: str, optional
    :param code: Time series code by which the return will be filtered.
    :type code: str, optional
    :param comment: Time series comment by which the return will be filtered.
    :type comment: str, optional
    :param name: Time series name by which the return will be filtered.
    :type name: str, optional
    :param numerica: Numeric? True or False.
    :type numerica: bool, optional
    :param theme_id: Theme by which the return will be filtered. For available themes run themes() function
    :type theme_id: str, optional
    :return: If no keyword is specified, returns a data frame containing all Ipeadata's time series. Else, returns only the ones that respects the specified parameters
    :rtype: pandas.DataFrame"""
    pos_fix = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix
    mdReturn = api_call(api).rename(index=str, columns={"TEMNOME": "THEME", "BASNOME": "BIG THEME", "FNTNOME": "SOURCE", "FNTSIGLA": "SOURCE ACRONYM", "FNTURL": "SOURCE URL", "MULNOME": "UNIT", "PAICODIGO": "COUNTRY", "PERNOME": "FREQUENCY", "SERATUALIZACAO": "LAST UPDATE", "SERCODIGO": "CODE", "SERCOMENTARIO": "COMMENT", "SERNOME": "NAME", "SERNUMERICA": "NUMERICA", "SERSTATUS": "SERIES STATUS", "TEMCODIGO": "THEME CODE", "UNINOME": "MEASURE"})
    if big_theme is not None:
        mdReturn = mdReturn.loc[mdReturn["BIG THEME"] == big_theme]
    if source is not None:
        mdReturn = mdReturn.loc[mdReturn["SOURCE ACRONYM"] == source]
    if country is not None:
        mdReturn = mdReturn.loc[mdReturn["COUNTRY"] == country]
    if frequency is not None:
        mdReturn = mdReturn.loc[mdReturn["FREQUENCY"] == frequency]
    if unit is not None:
        mdReturn = mdReturn.loc[mdReturn["UNIT"] == unit]
    if measure is not None:
        mdReturn = mdReturn.loc[mdReturn["MEASURE"] == measure]
    if source_ext is not None:
        mdReturn = mdReturn.loc[mdReturn["SOURCE"] == source_ext]
    if source_url is not None:
        mdReturn = mdReturn.loc[mdReturn["SOURCE URL"] == source_url]
    if last_update is not None:
        mdReturn = mdReturn.loc[mdReturn["LAST UPDATE"] == last_update]
    if code is not None:
        mdReturn = mdReturn.loc[mdReturn["CODE"] == code]
    if comment is not None:
        mdReturn = mdReturn.loc[mdReturn["COMMENT"] == comment]
    if name is not None:
        mdReturn = mdReturn.loc[mdReturn["NAME"] == name]
    if numerica is not None:
        mdReturn = mdReturn.loc[mdReturn["NUMERICA"] == numerica]
    if theme_id is not None:
        mdReturn = mdReturn.loc[mdReturn["THEME CODE"] == theme_id]
    return mdReturn
