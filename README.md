![ipeadatapy](https://user-images.githubusercontent.com/35273857/57802576-ad397100-772c-11e9-82fc-a30fc1fbe774.png)
# ipeadatapy: an API wrapper for Ipeadata
[![](https://img.shields.io/pypi/v/ipeadatapy.svg?color=blue&label=PyPI&style=popout-square)](https://pypi.org/project/ipeadatapy/) [![](https://img.shields.io/pypi/dm/ipeadatapy.svg?color=blue&style=flat-square)](https://pypi.org/project/ipeadatapy/)

# What is it?

The main purpose of Ipeadatapy package is to provide a way of extracting data from [Ipeadata](http://ipeadata.gov.br/Default.aspx) through Python using Ipeadata’s API. Thus, in this sense, Ipeadatapy is what is called an API wrapper. Nevertheless, the goal of the package is far from being only extract data. Ipeadatapy also is concerned with treating, cleaning and making more understandable the data provided by the API as well as providing data filtering and search mechanisms. Briefly, Ipeadatapy’s objective can be described as being to facilitate users to search and analyze time series data and metadata from Ipeadata database using Python.

# Main Features

Ipeadatapy allows you to extract processed data and metadata from Ipeadata's API in a more efficient and practical way, directly from your Python script, notebook and/or interactive shell. Here are some of the package's features:

- Lists in data frames all Ipeadata's available... 
  - Time series names and codes;
  - Sources;
  - Countries;
  - Territories;
  - Themes.
- Basic time series searching mechanism;
- Data filtering through defined functions parameters;
- Show time series data and metadata;
- Filter time series data set by day, month and/or year;
- Track latest updated time series.

Using pandas, one of the package dependecies, you can also plot and extract data and metadata. For more details check the [documentation](luanborelli.com/ipeadatapy/docs).

# Where to get it
The source code is currently hosted on [Ipeadatapy's GitHub](https://github.com/luanborelli/ipeadatapy/).

Binary installers for the latest released version are available at [Python package index page](https://pypi.org/project/ipeadatapy/).

`pip install ipeadatapy`

# Documentation
The official documentation is hosted on [author's website](http://www.luanborelli.net/): [luanborelli.com/ipeadatapy/docs](http://www.luanborelli.net/ipeadatapy/docs)

# Dependencies
The only dependecies are [pandas](https://github.com/pandas-dev/pandas)  and [requests](https://github.com/kennethreitz/requests). 

# License
[MIT](https://github.com/luanborelli/ipeadatapy/blob/master/LICENSE)
