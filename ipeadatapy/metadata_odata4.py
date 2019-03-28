import pandas as pd
from .api_call import api_call

def metadata_odata4(series=None):
    pos_fix = "('%s')" % series if series is not None else ""
    api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix
    return api_call(api).rename(index=str, columns={"TEMNOME": "THEME", "BASNOME": "BIG THEME", "FNTNOME": "SOURCE", "FNTSIGLA": "SOURCE ACRONYM", "FNTURL": "SOURCE URL", "MULNOME": "UNIT", "PAICODIGO": "COUNTRY", "PERNOME": "FREQUENCY", "SERATUALIZACAO": "LAST UPDATE", "SERCODIGO": "CODE", "SERCOMENTARIO": "COMMENT", "SERNOME": "NAME", "SERNUMERICA": "NUMERICA", "SERSTATUS": "SERIES STATUS", "TEMCODIGO": "THEME CODE", "UNINOME": "MEASURE"})
