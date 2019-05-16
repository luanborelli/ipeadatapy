themes
======================================

+------------------------------------------------------------------------------------------------------------------------+
| themes(theme_id=None, name=None, macro=None, regional=None, social=None)                                               |
+------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                        |
+----------+------------------+------------------------------------------------------------------------------------------+
| theme_id | int, optional    | Theme ID by which the return will be filtered                                            |
+----------+------------------+------------------------------------------------------------------------------------------+
| name     | str, optional    | Theme name by which the return will be filtered                                          |
+----------+------------------+------------------------------------------------------------------------------------------+
| macro    | int, optional    | If macro=1, the function will return only themes related to the Macroeconomics big theme |
+----------+------------------+------------------------------------------------------------------------------------------+
| regional | int, optional    | If regional=1, the function will return only themes related to the Regional big theme    |
+----------+------------------+------------------------------------------------------------------------------------------+
| social   | int, optional    | If social=1, the function will return only themes related to the Social big theme        |
+----------+------------------+------------------------------------------------------------------------------------------+
| return   | pandas.DataFrame | Returns available Ipeadata themes                                                        |
+----------+------------------+------------------------------------------------------------------------------------------+

`[source] <https://github.com/luanborelli/ipeadatapy/blob/master/ipeadatapy/themes.py>`__
