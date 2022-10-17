from pandas import DataFrame
from .api_call import api_call

cReturn = None


def countries(
    country_id: str = None, keyword: str = None, force_update: bool = False
) -> DataFrame:
    """
    Returns all Ipeadata available countries and country IDs.
    :param country_id: Country ID by which the return will be filtered.
    :type country_id: str, optional
    :param keyword: Keyword by which the return will be filtered.
    :type keyword: str, optional
    :return: Ipeadata available countries and country IDs.
    :rtype: pandas.DataFrame
    """
    global cReturn
    if force_update or cReturn is None:
        api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Paises"
        cReturn = api_call(api)[["PAICODIGO", "PAINOME"]].rename(
            index=str, columns={"PAICODIGO": "ID", "PAINOME": "COUNTRY"}
        )

    filtered_cReturn = cReturn.copy()

    if country_id is not None:
        filtered_cReturn = filtered_cReturn.loc[filtered_cReturn["ID"] == country_id]
    if keyword is not None:
        filtered_cReturn = filtered_cReturn[
            filtered_cReturn["COUNTRY"].str.contains(keyword)
        ]
    return filtered_cReturn
