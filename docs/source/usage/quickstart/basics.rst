The basics
======================================
Firt of all, you need to import the package:

>>> import ipeadatapy

======================================================
Finding and analyzing your desired time series
======================================================
Running this function will show all Ipeadata's time series:

>>> ipeadatapy.list_series()

If you are looking for series of a specific subject, you can filter the function output for only series containing some keyword. For example, let's filter the function return for only time series containing the word 'BPM6' in their names. This functionality can be used as a searching mechanism.

>>> ipeadatapy.list_series('BPM6')
                     CODE                                               NAME
6721              BPAG_AR             Ativos de reserva (Nova metod. - BPM6)
6722              BPAG_BC     Balanca comercial - Saldo (Nova metod. - BPM6)
6723             BPAG_BCM  Balanca comercial - Importacoes (Nova metod. -...
6724             BPAG_BCX  Balanca comercial - Exportacoes (Nova metod. -...
6725              BPAG_CF  Conta Financeira - Saldo (Captacoes - Concesso...
6726              BPAG_CK         Conta capital - Saldo (Nova metod. - BPM6)
6727             BPAG_CKD         Conta capital - Desp. (Nova metod. - BPM6)
6728             BPAG_CKR          Conta capital - Rec. (Nova metod. - BPM6)
6729            BPAG_CRCO  Outros invest. - Créd. comerciais e adiantamen...
6730           BPAG_CRCOA  Outros invest. - Créd. comerciais e adiantamen...
...                   ...                                                ...

You can also use any other keyword you want. Be aware of the case sensitiveness of the keyword.

======================================================
Getting more details
======================================================

Let's suppose that we found our desired time series. Its code is BPAG_AR. We can use a handy command called ``describe()`` to confirm the details about this time series.

>>> ipeadatapy.describe('BPAG_AR')
                           Ativos de reserva (Nova metod. - BPM6)
Name                       Ativos de reserva (Nova metod. - BPM6)
Code                                                      BPAG_AR
Big Theme                                          Macroeconomico
Theme                                       Balanco de pagamentos
Source          Banco Central do Brasil, Balanco de Pagamentos...
Source acronym                                    Bacen/BP (BPM6)
Comment         Metodologia do Manual de Balanco de Pagamentos...
Last update                         2019-03-14T13:48:00.803-03:00
Frequency                                                   Anual
Measure                                                       US$
Unit                                                      milhoes
Status                                                          A

As you can see, this function returns some details about the specified time series: the name of the series, his code, the big theme and theme which this series correspond, his source, the source acronym, the comment, his last update date and time, his frequency, measure, unit and status. Thus, this function is a good way to have an overview of a specific time series.

If you are not satisfied with these information, you can check a more complete metadata data frame about the series by running:

>>> ipeadatapy.metadata('BPAG_AR')
        BIG THEME FNTEXTURL       FNTID                                             SOURCE   SOURCE ACRONYM   ...   SERTEMMUN THEME CODE TEMCODIGOPAI                  THEME MEASURE
0  Macroeconômico      None  1333080354  Banco Central do Brasil, Balanço de Pagamentos...  Bacen/BP (BPM6)   ...        None         10         None  Balanço de pagamentos     US$


We will be digging deeper into the ``metadata()`` function in future sections.

======================================================
Observing the data
======================================================

Now that you are sure about your selected time series, you might be wondering how to observe what really matters: the data. For this purpose, use the function ``timeseries()``:

>>> ipeadatapy.timeseries('BPAG_AR')
    YEAR  DAY  MONTH     CODE                       DATE   VALUE (US$)
0   1995    1      1  BPAG_AR  1995-01-01T00:00:00-02:00  12918.900000
1   1996    1      1  BPAG_AR  1996-01-01T00:00:00-02:00   8666.100000
2   1997    1      1  BPAG_AR  1997-01-01T00:00:00-02:00  -7907.159127
3   1998    1      1  BPAG_AR  1998-01-01T00:00:00-02:00  -7970.207388
4   1999    1      1  BPAG_AR  1999-01-01T00:00:00-02:00  -7822.039996
5   2000    1      1  BPAG_AR  2000-01-01T00:00:00-02:00  -2261.654351
6   2001    1      1  BPAG_AR  2001-01-01T00:00:00-02:00   3306.600484
7   2002    1      1  BPAG_AR  2002-01-01T00:00:00-02:00    302.087225
8   2003    1      1  BPAG_AR  2003-01-01T00:00:00-02:00   8495.650494
9   2004    1      1  BPAG_AR  2004-01-01T00:00:00-02:00   2244.029835
10  2005    1      1  BPAG_AR  2005-01-01T00:00:00-02:00   4319.463872
11  2006    1      1  BPAG_AR  2006-01-01T00:00:00-02:00  30569.117416
12  2007    1      1  BPAG_AR  2007-01-01T00:00:00-02:00  87484.245682
13  2008    1      1  BPAG_AR  2008-01-01T00:00:00-02:00   2969.072068
14  2009    1      1  BPAG_AR  2009-01-01T00:00:00-02:00  46650.987800
15  2010    1      1  BPAG_AR  2010-01-01T00:00:00-02:00  49100.503587
16  2011    1      1  BPAG_AR  2011-01-01T00:00:00-02:00  58636.807211
17  2012    1      1  BPAG_AR  2012-01-01T00:00:00-02:00  18899.552358
18  2013    1      1  BPAG_AR  2013-01-01T00:00:00-02:00  -5926.487151
19  2014    1      1  BPAG_AR  2014-01-01T00:00:00-02:00  10832.657276
20  2015    1      1  BPAG_AR  2015-01-01T00:00:00-02:00   1568.772099
21  2016    1      1  BPAG_AR  2016-01-01T00:00:00-02:00   9237.436064
22  2017    1      1  BPAG_AR  2017-01-01T00:00:00-02:00   5092.868662
23  2018    1      1  BPAG_AR  2018-01-01T00:00:00-02:00   2927.674626
24  2019    1      1  BPAG_AR  2019-01-01T00:00:00-02:00    813.549854

======================================================
Observing intervals of the data
======================================================

If you just want the data for a specific year you can use the parameter ``year``:

>>> ipeadatapy.timeseries("GM366_ERC366", year=2019)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
12078  2019    2      1  GM366_ERC366  2019-01-02T00:00:00-02:00      3.8589
12079  2019    3      1  GM366_ERC366  2019-01-03T00:00:00-02:00      3.7677
12080  2019    4      1  GM366_ERC366  2019-01-04T00:00:00-02:00      3.7621
12081  2019    7      1  GM366_ERC366  2019-01-07T00:00:00-02:00      3.7056
12082  2019    8      1  GM366_ERC366  2019-01-08T00:00:00-02:00      3.7202
12083  2019    9      1  GM366_ERC366  2019-01-09T00:00:00-02:00      3.6925
12084  2019   10      1  GM366_ERC366  2019-01-10T00:00:00-02:00      3.6863
12085  2019   11      1  GM366_ERC366  2019-01-11T00:00:00-02:00      3.7135
12086  2019   14      1  GM366_ERC366  2019-01-14T00:00:00-02:00      3.7255
12087  2019   15      1  GM366_ERC366  2019-01-15T00:00:00-02:00      3.7043
...     ...  ...    ...           ...                        ...         ...
[89 rows x 6 columns]

If you just want the data for a specific month of a specific year, use both the parameters ``year`` and ``month``:

>>> ipeadatapy.timeseries("GM366_ERC366", year=2019, month=4)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
12139  2019    1      4  GM366_ERC366  2019-04-01T00:00:00-03:00      3.8676
12140  2019    2      4  GM366_ERC366  2019-04-02T00:00:00-03:00      3.8655
12141  2019    3      4  GM366_ERC366  2019-04-03T00:00:00-03:00      3.8430
12142  2019    4      4  GM366_ERC366  2019-04-04T00:00:00-03:00      3.8707
12143  2019    5      4  GM366_ERC366  2019-04-05T00:00:00-03:00      3.8616
12144  2019    8      4  GM366_ERC366  2019-04-08T00:00:00-03:00      3.8652
12145  2019    9      4  GM366_ERC366  2019-04-09T00:00:00-03:00      3.8557
12146  2019   10      4  GM366_ERC366  2019-04-10T00:00:00-03:00      3.8339
...     ...  ...    ...           ...                        ...         ...

Similarly, if you just want the data for a specific day of a specific month of a specific year use together the parameters ``year``, ``month`` and ``day``:

>>> ipeadatapy.timeseries("GM366_ERC366", year=2019, month=4, day=1)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
12139  2019    1      4  GM366_ERC366  2019-04-01T00:00:00-03:00      3.8676

Another option is to return only data relative to years greater than some year, say, 2017. For this, use the parameter ``yearGreaterThan``:

>>> ipeadatapy.timeseries("GM366_ERC366", yearGreaterThan=2017)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
11828  2018    2      1  GM366_ERC366  2018-01-02T00:00:00-02:00      3.2691
11829  2018    3      1  GM366_ERC366  2018-01-03T00:00:00-02:00      3.2529
11830  2018    4      1  GM366_ERC366  2018-01-04T00:00:00-02:00      3.2312
11831  2018    5      1  GM366_ERC366  2018-01-05T00:00:00-02:00      3.2403
11832  2018    8      1  GM366_ERC366  2018-01-08T00:00:00-02:00      3.2351
11833  2018    9      1  GM366_ERC366  2018-01-09T00:00:00-02:00      3.2391
11834  2018   10      1  GM366_ERC366  2018-01-10T00:00:00-02:00      3.2461
11835  2018   11      1  GM366_ERC366  2018-01-11T00:00:00-02:00      3.2295
11836  2018   12      1  GM366_ERC366  2018-01-12T00:00:00-02:00      3.2192
11837  2018   15      1  GM366_ERC366  2018-01-15T00:00:00-02:00      3.1957
...     ...  ...    ...           ...                        ...         ...
[340 rows x 6 columns]

You can also select an interval of years, say, from 2017 to 2018 using together with ``yearGreaterThan`` the parameter ``yearSmallerThan``:

>>> ipeadatapy.timeseries("GM366_ERC366", yearGreaterThan=2016, yearSmallerThan=2019)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
11579  2017    2      1  GM366_ERC366  2017-01-02T00:00:00-02:00      3.2723
11580  2017    3      1  GM366_ERC366  2017-01-03T00:00:00-02:00      3.2626
11581  2017    4      1  GM366_ERC366  2017-01-04T00:00:00-02:00      3.2327
11582  2017    5      1  GM366_ERC366  2017-01-05T00:00:00-02:00      3.2123
11583  2017    6      1  GM366_ERC366  2017-01-06T00:00:00-02:00      3.2051
11584  2017    9      1  GM366_ERC366  2017-01-09T00:00:00-02:00      3.2091
11585  2017   10      1  GM366_ERC366  2017-01-10T00:00:00-02:00      3.1912
11586  2017   11      1  GM366_ERC366  2017-01-11T00:00:00-02:00      3.2148
11587  2017   12      1  GM366_ERC366  2017-01-12T00:00:00-02:00      3.1655
11588  2017   13      1  GM366_ERC366  2017-01-13T00:00:00-02:00      3.2028
11589  2017   16      1  GM366_ERC366  2017-01-16T00:00:00-02:00      3.2228
11590  2017   17      1  GM366_ERC366  2017-01-17T00:00:00-02:00      3.2094
11591  2017   18      1  GM366_ERC366  2017-01-18T00:00:00-02:00      3.2205
11592  2017   19      1  GM366_ERC366  2017-01-19T00:00:00-02:00      3.2107
11593  2017   20      1  GM366_ERC366  2017-01-20T00:00:00-02:00      3.1912
...     ...  ...    ...           ...                        ...         ...
[499 rows x 6 columns]

The same logic applies to the parameters ``monthGreaterThan`` and ``monthSmallerThan``. For example, let's restrict the function output to an interval of months (e.g.: from june to december) for a specifc year, say, 2018:

>>> ipeadatapy.timeseries("GM366_ERC366", year=2018, monthGreaterThan=5, monthSmallerThan=13)
       YEAR  DAY  MONTH          CODE                       DATE  VALUE (R$)
11931  2018    1      6  GM366_ERC366  2018-06-01T00:00:00-03:00      3.7407
11932  2018    4      6  GM366_ERC366  2018-06-04T00:00:00-03:00      3.7418
11933  2018    5      6  GM366_ERC366  2018-06-05T00:00:00-03:00      3.7746
11934  2018    6      6  GM366_ERC366  2018-06-06T00:00:00-03:00      3.8187
11935  2018    7      6  GM366_ERC366  2018-06-07T00:00:00-03:00      3.8994
11936  2018    8      6  GM366_ERC366  2018-06-08T00:00:00-03:00      3.7853
11937  2018   11      6  GM366_ERC366  2018-06-11T00:00:00-03:00      3.6907
11938  2018   12      6  GM366_ERC366  2018-06-12T00:00:00-03:00      3.7038
11939  2018   13      6  GM366_ERC366  2018-06-13T00:00:00-03:00      3.7048
11940  2018   14      6  GM366_ERC366  2018-06-14T00:00:00-03:00      3.7051
11941  2018   15      6  GM366_ERC366  2018-06-15T00:00:00-03:00      3.7732
11942  2018   18      6  GM366_ERC366  2018-06-18T00:00:00-03:00      3.7537
11943  2018   19      6  GM366_ERC366  2018-06-19T00:00:00-03:00      3.7560
11944  2018   20      6  GM366_ERC366  2018-06-20T00:00:00-03:00      3.7329
...     ...  ...    ...           ...                        ...         ...
[147 rows x 6 columns]

From now on, use your creativity. There are a lot of possibilities with these parameter combinations. The available parameters for the function timeseries() can be found using the function ``help()``: ``help(ipeadatapy.timeseries)``.