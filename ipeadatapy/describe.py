import pandas as pd
from .metadata import metadata
from .metadata_old import metadata_old

def describe(series):
    """Describes the specified time series. series must be the time series' code."""
    desc_df = pd.DataFrame({list(metadata(series)['NAME'])[0]: [list(metadata(series)['NAME'])[0], list(metadata(series)['CODE'])[0], list(metadata_old(series)['BIG THEME'])[0], list(metadata_old(series)['THEME'])[0], list(metadata(series)['SOURCE'])[0], list(metadata(series)['SOURCE ACRONYM'])[0], list(metadata(series)['COMMENT'])[0], list(metadata(series)['LAST UPDATE'])[0], list(metadata(series)['FREQUENCY'])[0], list(metadata(series)['MEASURE'])[0], list(metadata(series)['UNIT'])[0], list(metadata(series)['SERIES STATUS'])[0]]}, index=['Name', 'Code', 'Big Theme', 'Theme', 'Source', 'Source acronym', 'Comment', 'Last update', 'Frequency', 'Measure', 'Unit', 'Status'])
    return desc_df
