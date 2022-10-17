from pandas import DataFrame
from .api_call import api_call

mdReturn = None


def metadata(
    series: str = None,
    big_theme: str = None,
    source: str = None,
    country: str = None,
    frequency: str = None,
    unit: str = None,
    measure: str = None,
    source_ext: str = None,
    source_url: str = None,
    last_update: str = None,
    code: str = None,
    comment: str = None,
    name: str = None,
    numerica: str = None,
    theme_id: str = None,
    force_update: bool = False,
) -> DataFrame:
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
    global mdReturn
    # Check if mdReturn has been initialized
    if force_update or mdReturn == None:
        pos_fix = "('%s')" % series if series is not None else ""
        api = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix

        mdReturn = api_call(api).rename(
            index=str,
            columns={
                "TEMNOME": "THEME",
                "BASNOME": "BIG THEME",
                "FNTNOME": "SOURCE",
                "FNTSIGLA": "SOURCE ACRONYM",
                "FNTURL": "SOURCE URL",
                "MULNOME": "UNIT",
                "PAICODIGO": "COUNTRY",
                "PERNOME": "FREQUENCY",
                "SERATUALIZACAO": "LAST UPDATE",
                "SERCODIGO": "CODE",
                "SERCOMENTARIO": "COMMENT",
                "SERNOME": "NAME",
                "SERNUMERICA": "NUMERICA",
                "SERSTATUS": "SERIES STATUS",
                "TEMCODIGO": "THEME CODE",
                "UNINOME": "MEASURE",
            },
        )

    filter_dict = {
        "BIG THEME": big_theme,
        "SOURCE ACRONYM": source,
        "COUNTRY": country,
        "FREQUENCY": frequency,
        "UNIT": unit,
        "MEASURE": measure,
        "SOURCE": source_ext,
        "SOURCE URL": source_url,
        "LAST UPDATE": last_update,
        "CODE": code,
        "COMMENT": comment,
        "NAME": name,
        "NUMERICA": numerica,
        "THEME CODE": theme_id,
    }

    # Filter the return
    filtered_mdReturn = mdReturn.copy()
    for key, value in filter_dict.items():
        if value is not None:
            filtered_mdReturn = filtered_mdReturn[filtered_mdReturn[key] == value]

    return filtered_mdReturn
