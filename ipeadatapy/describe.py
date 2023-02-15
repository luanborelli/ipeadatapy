import pandas as pd
from .metadata import metadata
from .metadata_old import metadata_old

def describe(series):
    """Describes the specified time series. series must be the time series' code."""
    series_metadata = metadata(series)
    desc_df = pd.DataFrame({list(series_metadata['NAME'])[0]: [list(series_metadata['NAME'])[0], list(series_metadata['CODE'])[0], list(series_metadata['BIG THEME'])[0], list(series_metadata['THEME CODE'])[0], list(series_metadata['SOURCE'])[0], list(series_metadata['SOURCE ACRONYM'])[0], list(series_metadata['COMMENT'])[0], list(series_metadata['LAST UPDATE'])[0], list(series_metadata['FREQUENCY'])[0], list(series_metadata['MEASURE'])[0], list(series_metadata['UNIT'])[0], list(series_metadata['SERIES STATUS'])[0]]}, index=['Name', 'Code', 'Big Theme', 'Theme code', 'Source', 'Source acronym', 'Comment', 'Last update', 'Frequency', 'Measure', 'Unit', 'Status'])
    return desc_df
