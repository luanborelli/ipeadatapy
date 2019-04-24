The basics
======================================

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

Now that you are sure about your selected time series, you might be wondering how to observe what really matters: the data. For this, simply run:

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

Now that you know how to search for a series, to verify his details and metadata and to display his data, maybe you are interested in visualizing and extracting them. We will cover these aspects in the next section.