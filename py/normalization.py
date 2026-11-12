import pandas as pd
data=pd.read_csv("data.csv")
#print(data.columns)

ch=int(input("Enter the choice"))
if ch==1:
    numeric_col=data.select_dtypes(include=["int64","float64"]).columns
    print(numeric_col.tolist())
    col=input("Enter the col")
    if col in data.columns:
        max=data[col].max()
        min=data[col].min()
        data["MinMax"]=(data[col]-min)/(max-min)
        print(data["MinMax"])
elif ch==2:
    numeric_col=data.select_dtypes(include=["int64","float64"]).columns
    print(numeric_col.tolist())
    col=input("Enter the col")
    if col in data.columns:
        mean=data[col].mean()
        std=data[col].std()
        data["Z_sc"]=(data[col]-mean)/std
        print(data["Z_sc"])
    
