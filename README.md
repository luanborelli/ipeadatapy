# ipeadatapy
# What is it?
ipeadatapy is a data and metadata extraction package made in Python using Ipeadata database official API.

# Main Features
- List Ipeadata series names and codes with `ipeadatapy.list_series()`
- Search for series by name using `ipeadatapy.list_series('SERIES NAME')`
- Describe Ipeadata series using `ipeadatapy.describe('SERIES CODE')`
- Show Ipeadata series data using `ipeadatapy.dataseries('SERIES CODE')`
- List Ipeadata series sources using `ipeadatapy.fontes()`

# Where to get it
The source code is currently hosted on GitHub at: https://github.com/luanborelli/ipeadatapy/  
Binary installers for the latest released version are available at the Python package index.

`pip install ipeadatapy`

# Dependencies
- [pandas](https://github.com/pandas-dev/pandas)  
- [requests](https://github.com/kennethreitz/requests)  
