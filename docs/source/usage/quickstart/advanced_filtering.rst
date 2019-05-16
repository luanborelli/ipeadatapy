Advanced filtering using metadata
======================================

======================================================
The metadata() function
======================================================

Now that you have knowledge of some of the metadata of Ipeadata, let's introduce yourself to a function called ``metadata()``. This function returns all Ipeadata's time series in a data frame, similarly to the ``list_series()`` function. However, the difference between the two functions is that ``metadata()`` returns not only the time series but also their metadata. You might then be asking yourself why these two functions exists, since ``metadata()`` is a more complete version of the ``list_series()`` function (``metadata()`` features all of the ``list_series()`` information plus metadata). The answer is: ``list_series()`` is intended to be a more simplistic version, aiming unexperienced users and designed to be friendly to them. ``metadata()``, in fact, is a more complete version as well as more confusing because of the quantity of information returned. No more words, let's run the function:

>>> ipeadatapy.metadata()
           BIG THEME                                             SOURCE SOURCE ACRONYM            ...            SERIES STATUS THEME CODE                   MEASURE
0     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
1     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
2     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
3     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                    Cabeça
4     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                    Cabeça
5     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                    Cabeça
6     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        I          1                  Tonelada
7     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
8     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
9     Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
10    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
11    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
12    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                  Tonelada
13    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        I          1                  Tonelada
14    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        I          1                    Cabeça
15    Macroeconômico  Instituto Brasileiro de Geografia e Estatístic...    IBGE/Coagro            ...                        A          1                    Cabeça
...              ...                                                ...            ...            ...                      ...        ...                       ...
[8549 rows x 15 columns]

======================================================
Better filtering with metadata()
======================================================

Why is this function so powerful and important? The first obvious answer is: it gives you more informations about time series. The not-so-obvious answer is: it allows you to better filter time series from Ipeadata. Let's state an illustrative problem for better understanding:

	`Ipeadata API has 8565 time series in total. Let's suppose you are doing research in macroeconomics about the United States, but for some specific reason, your interest in data is restricted to data published by The 	Economist. It also needs to be quarterly published. How to solve this problem using ipeadatapy Python package?`

>>> ipeadatapy.metadata(big_theme="Macroeconômico", country="USA", source="Economist", frequency="Trimestral")
           BIG THEME         SOURCE SOURCE ACRONYM         SOURCE URL     UNIT    ...                                                  NAME NUMERICA SERIES STATUS THEME CODE   MEASURE
5585  Macroeconômico  The Economist      Economist  www.economist.com  bilhões    ...     balanço - conta corrente - saldo (acum. 12 meses)     True             I         11       US$
5586  Macroeconômico  The Economist      Economist  www.economist.com     None    ...                   PIB - var. real trimestral anualiz.     True             A         11  (% a.a.)
5587  Macroeconômico  The Economist      Economist  www.economist.com     None    ...     PIB - var. real contra igual trimestre do ano ...     True             A         11  (% a.a.)
[3 rows x 15 columns]

Gotcha! Other metadata also can be used as filtering parameters. For all parameters run ``help(idpy.metadata)``.