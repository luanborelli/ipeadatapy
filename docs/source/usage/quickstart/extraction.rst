Data Extraction
======================================

In this section we will show you how to extract data from ipeadatapy using the package together with one of his dependencies (pandas) and other Python Built-In features.  One of the most useful aspects of having an API wrapper is to have the option of extracting data in a more efficient and practical way than extracting the same data from the database's website. With this package it's possible to extract not only data but also quantitative and descriptive metadatas from Ipeadata database. As we will see, you can even extract mass quantities of spreadsheets at once, being also possible extraction filterings accordingly to your needs. Let's start with the basics.

#################################
Extracting one single time series
#################################

Let's first import ipeadatapy package.

>>> import ipeadatapy

then, let's suppose that we already know which time series we want to extract and already found his code using the list_series() function. Let, e.g., this time series be the one which the code is GM366_ERC366. Thus, we can show the data calling the following function: 

>>> ipeadatapy.timeseries('GM366_ERC366')
       YEAR  DAY  MONTH          CODE                       DATE    VALUE (R$)
0      1985    2      1  GM366_ERC366  1985-01-02T00:00:00-02:00  1.152000e-09
1      1985    3      1  GM366_ERC366  1985-01-03T00:00:00-02:00  1.152000e-09
2      1985    4      1  GM366_ERC366  1985-01-04T00:00:00-02:00  1.152000e-09
3      1985    5      1  GM366_ERC366  1985-01-05T00:00:00-02:00           NaN
...     ...  ...    ...           ...                        ...           ...

To extract this dataframe as a .xlsx file you simply do:

>>> ipeadatapy.timeseries('GM366_ERC366').to_excel('.../path/yourFileName.xlsx')

If you prefer, you can extract the data in csv format instead of xlsx. For this, you can use the function called '.to_csv()':

>>> ipeadatapy.timeseries('GM366_ERC366').to_csv('.../path/yourFileName.csv', sep=';')

where '.../path/' represents the desired directory path where the file will be placed and 'yourFile.csv' the name of the file. If you just set the file name without a directory path, then the file will be saved in the directory where you are running your Python. Pay attention to not omit the filename extensions, '.csv' or '.xlsx'.

########################################
Extracting multiple time series at once
########################################

Let's suppose that we want to extract more than one time series at once. We can do it by defining a list containing the codes of the time series that we want to extract then running a 'for' structure that will loop through this list, extracting a file for each of the timeseries contained there. For illustration purposes, let's suppose that we want to extract these three timeseries: GM366_ERC366, IBMEC12_TJTIT12 and PIBE. Then we need to define a list containing them:

>>> timeseries = ['GM366_ERC366', 'IBMEC12_TJTIT12', 'PIBE']

Now, let's define a 'for' loop to extract these series:

>>> for i in timeseries:
	ipeadatapy.timeseries(i).to_csv(i + '.csv', sep=';') 

The output will be three '.csv' files: GM366_ERC366.csv, IBMEC12_TJTIT12.csv and PIBE.csv, saved in the directory where you runned your Python. 

#################################
Extracting other kinds of data
#################################

Ipeadatapy's functions were defined to always return data in the form of data frames. Thus, every function output can be extracted using pandas' .to_csv() or .to_excel() functions in the same way we've shown in the past example. 