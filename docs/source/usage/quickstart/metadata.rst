Metadata
======================================

Every Ipeadata's time series is accompanied by a set of metadata. Metadata are data about data. Some examples of the elements of this set of metadata are country, big theme, theme, source and unit of measure. Some specific kinds of metadata have their own function on Ipeadata API. Let's see some of them:

======================================================
Countries
======================================================

You can have a look at the available Ipeadata's countries by running the ``countries()`` function:

>>> ipeadatapy.countries()
      ID                         COUNTRY
0    ZAF                   África do Sul
1    DEU                        Alemanha
2   LATI                  América Latina
3    AGO                          Angola
4    SAU                  Arábia Saudita
5    DZA                         Argélia
6    ARG                       Argentina
7    AUS                       Austrália
8    AUT                         Áustria
9    BEL                         Bélgica
10   BOL                         Bolívia
..   ...                             ...

======================================================
Themes
======================================================

You can also have a look on the available themes for Ipeadata using the function ``themes()``:

>>> ipeadatapy.themes()
    ID                     NAME  MACRO  REGIONAL  SOCIAL
0   28             Agropecuária    NaN       1.0     NaN
1   23       Assistência social    NaN       NaN     1.0
2   25     Avaliação do governo    NaN       NaN     NaN
3   10    Balanço de pagamentos    1.0       NaN     NaN
4    7                   Câmbio    1.0       NaN     NaN
5    5        Comércio exterior    1.0       1.0     NaN
6    2         Consumo e vendas    1.0       1.0     NaN
7    8         Contas nacionais    1.0       NaN     NaN
8   81         Contas Regionais    NaN       1.0     NaN
9   24       Correção monetária    1.0       NaN     NaN
10  37               Demografia    NaN       NaN     1.0
..  ..                      ...    ...       ...     ...


Let's suppose you have the interest to know which of the themes of Ipeadata are related to the Macroeconomics big theme. The parameter ``macro`` will solve this problem:

>>> ipeadatapy.themes(macro=1)
    ID                     NAME  MACRO  REGIONAL  SOCIAL
3   10    Balanço de pagamentos    1.0       NaN     NaN
4    7                   Câmbio    1.0       NaN     NaN
5    5        Comércio exterior    1.0       1.0     NaN
6    2         Consumo e vendas    1.0       1.0     NaN
7    8         Contas nacionais    1.0       NaN     NaN
9   24       Correção monetária    1.0       NaN     NaN
..  ..                      ...    ...       ...     ...

Let's now suppose that you just want the function to return themes that are related both to the macroeconomics and regional themes. For this, use ``macro`` and ``regional`` parameters together:

>>> ipeadatapy.themes(macro=1, regional=1)
    ID                NAME  MACRO  REGIONAL  SOCIAL
5    5   Comércio exterior    1.0       1.0     NaN
6    2    Consumo e vendas    1.0       1.0     NaN
18  12             Emprego    1.0       1.0     NaN
19  19  Estoque de capital    1.0       1.0     NaN
20   6   Finanças públicas    1.0       1.0     NaN
31   3     Moeda e crédito    1.0       1.0     NaN
33  14           População    1.0       1.0     NaN
34   9              Preços    1.0       1.0     NaN
37   1            Produção    1.0       1.0     NaN
45  33          Transporte    1.0       1.0     NaN
..  ..                 ...    ...       ...     ...


The parameter ``social`` is also available and works in the same way of macro and regional. For more parameters available for the function ``themes()`` run ``help(idpy.themes)``.

======================================================
Sources
======================================================

Other important metadata is the source. This metadata have his own functions, ``sources()``. Let's have a look:

>>> ipeadatapy.sources()
0                         Abia
1                       Abinee
2                         ABPO
3                      Abracal
4                        Abras
5                    ACSP/IEGV
6                         Anac
7                       Anatel
8                       Anbima
9                       Anbima
10                        Anda
..                         ...


======================================================
Territories
======================================================

For regional time series we also have some information about Brazilian territories through the function ``territories()``:

>>> ipeadatapy.territories()
                                                    NAME            ID   ...          AREA  CAPITAL
0                                         (não definido)                 ...           NaN     None
1                                                 Brasil             0   ...     8531507.6    False
2                                           Região Norte             1   ...     3869637.9    False
3                                               Rondônia            11   ...      238512.8    False
4                                  Alta Floresta D'Oeste       1100015   ...        7111.8    False
5                                              Ariquemes       1100023   ...        4995.3    False
6                                                 Cabixi       1100031   ...        1530.7    False
7                                                 Cacoal       1100049   ...        3808.4    False
8                                             Cerejeiras       1100056   ...        2645.0    False
9                                      Colorado do Oeste       1100064   ...        1442.4    False
10                                            Corumbiara       1100072   ...        3079.7    False
...                                                  ...           ...   ...           ...      ...


Two interesting parameters of ``territories()`` function are ``areaGreaterThan`` and ``areaSmallerThan``. With these parameters, it is possible to filter the return of the function for just territories greater than, smaller than or between the specified parameters. For example, let's check which of the Brazilian territories have the area greater than 1000000:

>>> ipeadatapy.territories(areaGreaterThan=1000000)
                      NAME                  ID        LEVEL       AREA CAPITAL
1                   Brasil                   0       Brasil  8531507.6   False
2             Região Norte                   1      Regiões  3869637.9   False
138               Amazonas                  13      Estados  1577820.2   False
386                   Pará                  15      Estados  1253164.5   False
1161       Região Nordeste                   2      Regiões  1558200.4   False
17960  Região Centro-oeste                   5      Regiões  1612077.2   False
18452     AMC1872_1997 001  513AMC1872_1997001  AMC 1872-00  1947986.1    None
18454          AMC2097 001        51AMC2097001    AMC 20-00  1061175.7    None

Let's now check the territories which the area is between 1000000 and 1100000:

>>> ipeadatapy.territories(areaGreaterThan=1000000, areaSmallerThan=1500000)
              NAME            ID      LEVEL       AREA CAPITAL
386           Pará            15    Estados  1253164.5   False
18454  AMC2097 001  51AMC2097001  AMC 20-00  1061175.7    None

======================================================
Other metadata
======================================================

Although only 4 metadata from Ipeadata have their own function, there are a lot more metadata available for the data base time series. The function ``metadata()`` returns all Ipeadata time series in a data frame with all of his metadata. Each of the collumns of the data frame represents a metadata. 

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

As you can see, this data frame is too big to be represented here. His dimension is 8549 rows by 15 columns. Each of these columns represents one metadata. The columns are BIG THEME, SOURCE, SOURCE ACRONYM, SOURCE URL, UNIT, COUNTRY, FREQUENCY, LAST UPDATE, CODE, COMMENT, NAME, NUMERICA, SERIES STATUS, THEME CODE, and MEASURE. In the next section, we will learn how to use these metadata as filtering options to improve our research.