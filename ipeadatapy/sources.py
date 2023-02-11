from functools import lru_cache
from pandas import DataFrame
from .api_call import api_call


@lru_cache(maxsize=32)
def sources() -> DataFrame:
    """
    Returns available Ipeadata's sources in the form of a data frame.
    :return: Ipeadata's sources in the form of a data frame.
    :rtype: pandas.DataFrame
    """
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Fontes"
    return api_call(api).rename(
        index=str, columns={"FNTID": "ID", "FNTSIGLA": "SIGLA"}
    )["SIGLA"]
