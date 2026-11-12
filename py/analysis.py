import pandas as pd

data=pd.read_csv("data.csv")

print(data)

print(data.head())

print(data.tail())

print(data.describe())

print(data.shape)

print(data.info())

print(data.isnull().sum())

print(data.notnull().sum())


col=input("Enter the column name")
if col in data.columns:
    print(data[col])

