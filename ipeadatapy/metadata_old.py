import pandas as pd
from .api_call import api_call

def metadata_old(series=None):
    """If no keyword is specified, returns a data frame containing all Ipeadata's time series. Else, returns only the ones that contains the specified keyword in their names."""
    url_final = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/v1/Metadados%s" % url_final
    return api_call(api).rename(index=str, columns={"TEMNOME": "THEME", "BASNOME": "BIG THEME", "FNTNOME": "SOURCE", "FNTSIGLA": "SOURCE ACRONYM", "FNTURL": "SOURCE URL", "MULNOME": "UNIT", "PAICODIGO": "COUNTRY", "PERNOME": "FREQUENCY", "SERATUALIZACAO": "LAST UPDATE", "SERCODIGO": "CODE", "SERCOMENTARIO": "COMMENT", "SERNOME": "NAME", "SERNUMERICA": "NUMERICA", "SERSTATUS": "SERIES STATUS", "TEMCODIGO": "THEME CODE", "UNINOME": "MEASURE"})
