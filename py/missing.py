import pandas as pd

data=pd.read_csv("data.csv")

#display
print(data)

#missing value
print(data.isnull())

#missing value sum
print(data.isnull().sum())

#missing value Total
print(data.isnull().sum().sum())

#dropna
data=data.dropna()
print(data)

#drop column
data=data.dropna(axis=1)
print(data)

#fillna
data=data.fillna(0)
print(data)

#notnull
data=data.notnull().sum()
print(data)
