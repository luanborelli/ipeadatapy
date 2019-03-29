# ipeadatapy
[![](https://img.shields.io/pypi/v/ipeadatapy.svg?color=blue&label=PyPI&style=popout-square)](https://pypi.org/project/ipeadatapy/) [![](https://img.shields.io/pypi/dm/ipeadatapy.svg?color=blue&style=flat-square)](https://pypi.org/project/ipeadatapy/)
# What is it?
ipeadatapy is a data and metadata manipulation, visualization and extraction package made in Python using Ipeadata database official API. In it's essence it is an API wrapper.

# Main Features

Ipeadatapy allows you to manipulate, visualize and extract data and metadata from Ipeadata's database in a more efficient and practical way, directly from your Python script, notebook and/or interactive shell. Here are some of the package's features:

- Searches for time series by name using `ipeadatapy.list_series('SERIES NAME')`;
- Describes Ipeadata's time series using `ipeadatapy.describe('SERIES CODE')`;
- Shows Ipeadata's time series data using `ipeadatapy.dataseries('SERIES CODE')`;
- Lists in a dataframe Ipeadata's... 
  - time series names and codes using `ipeadatapy.list_series()`;
  - time series sources using `ipeadatapy.sources()`;
  - time series update date from the most to the least recently updated using `ipeadatapy.latest_updates()`. This function also returns the number of time series updated on the current day.;
  - available countries using `ipeadatapy.countries()`;
  - available territories using `ipeadatapy.territories()`;
  - available themes using `ipeadatapy.themes()`.

# Where to get it
The source code is currently hosted on [Ipeadatapy's GitHub](https://github.com/luanborelli/ipeadatapy/).

Binary installers for the latest released version are available at [Python package index page](https://pypi.org/project/ipeadatapy/).

`pip install ipeadatapy`

# Dependencies
The only dependecies are [pandas](https://github.com/pandas-dev/pandas)  and [requests](https://github.com/kennethreitz/requests). 
