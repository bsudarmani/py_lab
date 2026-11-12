
import pandas as pd

data = pd.read_csv("data.csv")

print("Numeric Columns:")
print(data.select_dtypes(include=["number"]).columns.tolist())

col1 = input("Enter first column: ")
col2 = input("Enter second column: ")

if col1 in data.columns and col2 in data.columns:

    # Correlation
    corr = data[col1].corr(data[col2])

    # Covariance
    cov = data[col1].cov(data[col2])

    print("Correlation:", corr)
    print("Covariance:", cov)

else:
    print("Invalid column name")



=====================================================================
import pandas as pd
import math

data = pd.read_csv("data.csv")

# User-defined Correlation function
def correlation(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = 0
    sum_x = 0
    sum_y = 0

    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        sum_x += (x[i] - mean_x) ** 2
        sum_y += (y[i] - mean_y) ** 2

    result = numerator / math.sqrt(sum_x * sum_y)

    return result


# User-defined Covariance function
def covariance(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    total = 0

    for i in range(n):
        total += (x[i] - mean_x) * (y[i] - mean_y)

    return total / (n - 1)


# Main Program
print(data.select_dtypes(include=["number"]).columns.tolist())

col1 = input("Enter first column: ")
col2 = input("Enter second column: ")

if col1 in data.columns and col2 in data.columns:

    x = data[col1].tolist()
    y = data[col2].tolist()

    print("Correlation:", correlation(x, y))
    print("Covariance:", covariance(x, y))

else:
    print("Invalid column")
