# ipeadatapy
# What is it?
ipeadatapy is a data and metadata extraction package made in Python using Ipeadata database official API.

# Main Features
- Lists Ipeadata's timeseries names and codes with `ipeadatapy.list_series()`
- Searches for timeseries by name using `ipeadatapy.list_series('SERIES NAME')`
- Describes Ipeadata's timeseries using `ipeadatapy.describe('SERIES CODE')`
- Shows Ipeadata's timeseries data using `ipeadatapy.dataseries('SERIES CODE')`
- Lists Ipeadata's timeseries sources using `ipeadatapy.sources()`
- Lists Ipeadata's timeseries update date from the most to the least recently updated using `ipeadatapy.last_updated()`. This function also returns the number of timeseries updated on the current day.

# Where to get it
The source code is currently hosted on GitHub at: https://github.com/luanborelli/ipeadatapy/  
Binary installers for the latest released version are available at the Python package index.

`pip install ipeadatapy`

# Dependencies
- [pandas](https://github.com/pandas-dev/pandas)  
- [requests](https://github.com/kennethreitz/requests)  
