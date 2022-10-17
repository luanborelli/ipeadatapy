import requests as req
from pandas import DataFrame


def api_call(api: str) -> DataFrame:
    """
    For advanced users. Returns raw Ipeadata API data in the form of a data frame.
    :param api: Ipeadata API URL.
    :type api: str
    :return: Ipeadata API data in the form of a data frame.
    :rtype: pandas.DataFrame
    """
    response = req.get(api)
    if response.status_code == req.codes.ok:
        json_response = response.json()
        if "value" in json_response:
            try:
                data_frame = DataFrame(json_response["value"])
                return data_frame
            except Exception:
                return None
    return None
