import pandas as pd
from .api_call import api_call

def metadata(series=None, big_theme=None, source=None, country=None, frequency=None, unit=None, measure=None, status=None, source_ext=None, source_url=None, last_update=None, code=None, comment=None, name=None, numerica=None, theme_code=None):
    """If no keyword is specified, returns a data frame containing all Ipeadata's time series. Else, returns only the ones that contains the specified keyword in their names."""
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
    if theme_code is not None:
        mdReturn = mdReturn.loc[mdReturn["THEME CODE"] == theme_code]
    return mdReturn
