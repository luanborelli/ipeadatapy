import pandas as pd
from .metadata_odata4 import metadata_odata4
from .metadata import metadata

def describe(series):
    desc_df = pd.DataFrame({list(metadata_odata4(series)['NAME'])[0]: [list(metadata_odata4(series)['NAME'])[0], list(metadata_odata4(series)['CODE'])[0], list(metadata(series)['BIG THEME'])[0], list(metadata(series)['THEME'])[0], list(metadata_odata4(series)['SOURCE'])[0], list(metadata_odata4(series)['SOURCE ACRONYM'])[0], list(metadata_odata4(series)['COMMENT'])[0], list(metadata_odata4(series)['LAST UPDATE'])[0], list(metadata_odata4(series)['FREQUENCY'])[0], list(metadata_odata4(series)['MEASURE'])[0], list(metadata_odata4(series)['UNIT'])[0], list(metadata_odata4(series)['SERIES STATUS'])[0]]}, index=['Name', 'Code', 'Big Theme', 'Theme', 'Source', 'Source acronym', 'Comment', 'Last update', 'Frequency', 'Measure', 'Unit', 'Status'])
    return desc_df
