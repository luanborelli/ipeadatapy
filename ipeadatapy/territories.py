from pandas import DataFrame
from .api_call import api_call

tReturn = None


def territories(
    name: str = None,
    level: str = None,
    territory_id: str = None,
    area: float = None,
    areaGreaterThan: float = None,
    areaSmallerThan: float = None,
    capital: bool = None,
    force_update: bool = False,
) -> DataFrame:
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
    global tReturn
    if force_update or tReturn is None:
        api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Territorios"
        tReturn = api_call(api)[
            ["TERNOME", "TERCODIGO", "NIVNOME", "TERAREA", "TERCAPITAL"]
        ].rename(
            index=str,
            columns={
                "TERNOME": "NAME",
                "TERCODIGO": "ID",
                "NIVNOME": "LEVEL",
                "TERAREA": "AREA",
                "TERCAPITAL": "CAPITAL",
            },
        )

    filter_dict = {
        "NAME": name,
        "LEVEL": level,
        "ID": territory_id,
        "AREA": area,
        "CAPITAL": capital,
    }
    filtered_tReturn = tReturn.copy()

    for key, value in filter_dict.items():
        if value is not None:
            filtered_tReturn = filtered_tReturn.loc[filtered_tReturn[key] == value]

    if areaGreaterThan is not None:
        filtered_tReturn = filtered_tReturn.loc[
            filtered_tReturn["AREA"] > areaGreaterThan
        ]
    if areaSmallerThan is not None:
        filtered_tReturn = filtered_tReturn.loc[
            filtered_tReturn["AREA"] < areaSmallerThan
        ]

    return filtered_tReturn
