metadata
======================================

+------------------------------------------------------------------------------------------------------+
|                                         metadata(series=None)                                        |
+------------------------------------------------------------------------------------------------------+
| If no series is specified, returns a data frame containing all metadata of all Ipeadata time series. |
|    Else, returns only the specified time series' metadata. `series` must be the time series' code.   |
+-------------------------------------------------------+----------------------------------------------+
|                       **series**                      |                      str                     |
+-------------------------------------------------------+----------------------------------------------+
`[source] <https://github.com/luanborelli/ipeadatapy/blob/master/ipeadatapy/metadata.py>`__

+------------------------------------------------------------------------------------------------------+
|                                     metadata_odata4(series=None)                                     |
+------------------------------------------------------------------------------------------------------+
| If no series is specified, returns a data frame containing all metadata of all Ipeadata time series. |
|    Else, returns only the specified time series' metadata. `series` must be the time series' code.   |
+------------------------------------------------------+-----------------------------------------------+
|                      **series**                      |                      str                      |
+------------------------------------------------------+-----------------------------------------------+
`[source] <https://github.com/luanborelli/ipeadatapy/blob/master/ipeadatapy/metadata_odata4.py>`__

**Notes**: the difference between the two functions is strictly technical and related to the API. If in some aspect you are having trouble with one of the functions, try the another.