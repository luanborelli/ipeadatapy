import requests as req
import pandas as pd

def api_call(api):
    response = req.get(api)
    if response.status_code == req.codes.ok:
        json_response = response.json()
        if 'value' in json_response:
            try:
                data_frame = pd.DataFrame(json_response['value'])
                return data_frame
            except Exception:
                return None
    return None
