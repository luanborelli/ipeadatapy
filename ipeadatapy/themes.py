from pandas import DataFrame
from .api_call import api_call

thReturn = None


def themes(
    theme_id: int = None,
    name: str = None,
    macro: int = None,
    regional: int = None,
    social: int = None,
    force_update: bool = False,
) -> DataFrame:
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
    global thReturn
    if force_update or thReturn is None:
        api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Temas"
        thReturn = api_call(api)[
            ["TEMCODIGO", "TEMNOME", "MACRO", "REGIONAL", "SOCIAL"]
        ].rename(index=str, columns={"TEMCODIGO": "ID", "TEMNOME": "NAME"})

    filter_dict = {
        "ID": theme_id,
        "NAME": name,
        "MACRO": macro,
        "REGIONAL": regional,
        "SOCIAL": social,
    }
    filtered_thReturn = thReturn.copy()

    for key, value in filter_dict.items():
        if value is not None:
            filtered_thReturn = filtered_thReturn.loc[filtered_thReturn[key] == value]
    return filtered_thReturn
