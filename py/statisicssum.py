import pandas as pd

data=pd.read_csv("data.csv")


print(data)

print(data.mean(numeric_only=True))

print(data.median(numeric_only=True))

print(data.mode().iloc[1])

print(data.std(numeric_only=True))

print(data.describe())

print(data.min(numeric_only=True))

print(data.max(numeric_only=True))

print(data.var(numeric_only=True))

print(data.sum(numeric_only=True))

print(data.count())
