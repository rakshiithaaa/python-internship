import pandas as pd
data = pd.read_csv('C:\\Data Analysis & Python\\01.Data Cleaning and Preprocessing.csv')

pandas.core.frame.DataFrame
data.info #consice summary
data.describe #descriptive statistics
data = data.drop_duplicates()
data
data.isnull()
data.isnull().sum()
data.notnull()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
data2
data2.isnull().sum().sum()
data
data2
data3 = data.fillna(method = 'pad')
data3
data4 = data.fillna(method = 'bfill')
data4
