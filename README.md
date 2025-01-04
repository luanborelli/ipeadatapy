![ipeadatapy](logo.png)
# ipeadatapy: an API wrapper for Ipeadata
[![](https://img.shields.io/pypi/v/ipeadatapy.svg?color=blue&label=PyPI&style=popout-square)](https://pypi.org/project/ipeadatapy/) [![Downloads](https://pepy.tech/badge/ipeadatapy)](https://pepy.tech/project/ipeadatapy)

# What is it?

The primary purpose of the Ipeadatapy package is to provide a way to extract data from [Ipeadata](http://ipeadata.gov.br/Default.aspx) via Python, using Ipeadata's [API](http://ipeadata.gov.br/api/). In this regard, Ipeadatapy acts as an API wrapper. However, the package’s objectives go beyond merely extracting raw data. Ipeadatapy also focuses on pre-processing, cleaning, and enhancing the usability of the API's data, as well as offering data search and filtering capabilities. In short, Ipeadatapy aims to simplify the process for users to search and analyze data and metadata from the Ipeadata database using Python.

# Main Features

Ipeadatapy enables users to extract processed data and metadata from Ipeadata's API directly from Python scripts, notebooks, or interactive shells in a more efficient and practical manner than using Ipeadata's official website. Some of the package's features allow users to:

- List all of Ipeadata's available:
  - Time series (names and codes);
  - Data sources;
  - Data "themes";
  - Countries with available data;
  - Territories with available data.
- Search for time series data using keywords;
- Filter data using several predefined filtering parameters;
- Display a given time series data and metadata;
- Filter time series data periods by day, month, and/or year;
- Track the latest Ipeadata's updated time series.

With [pandas](https://pandas.pydata.org/), one of the package's dependencies, you can also plot and extract data and metadata. For more details, check the [documentation](http://www.luanborelli.net/ipeadatapy/docs).  

# Where to get it

The source code is currently hosted on [Ipeadatapy's GitHub](https://github.com/luanborelli/ipeadatapy/).

Binary installers for the latest released version are available at [Python package index page](https://pypi.org/project/ipeadatapy/).

`pip install ipeadatapy`

# Documentation

The official documentation is available on [luanborelli.com/ipeadatapy/docs](http://www.luanborelli.net/ipeadatapy/docs).

# Dependencies

The only dependecies are [pandas](https://github.com/pandas-dev/pandas) and [requests](https://github.com/kennethreitz/requests). 

# License
[MIT](https://github.com/luanborelli/ipeadatapy/blob/master/LICENSE)
