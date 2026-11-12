import pandas as pd

n=int(input("Enter the number"))
data=[]
for i in range(n):
    pid=int(input("Enter the product id:"))
    pname=input("Enter the product name:")
    price=float(input("Enter the price amount"))
    stock=int(input("Enter the stock amount"))
    data.append([pid,pname,price,stock])

#print(data)
df=pd.DataFrame(data,columns=[
    "pr_id",
    "p_name",
    "price",
    "stock"
    ])
#display
print(df.head())
print(df.tail())
print("Display DataFrame")
print(df)

print("IsNUll")
print(df.isnull())

print("Not nulll")
print(df.notnull())

print("product Name")
print(df["p_name"])

print("product sum")
print(df["price"].sum())

print("condition based")
price=float(input("Enter the price amount"))
res=df[df["price"]>price]
print(res)

print("Discount")
discount=float(input("Enter the discount amount"))
res1=df["price"]*discount/100
print(res)

