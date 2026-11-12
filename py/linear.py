from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split 

data=pd.read_csv("house.csv")
#print(data)

#print(data.head())

x=data[["area_sqft","bedrooms","bathrooms","house_age_years"]]
y=data["price_inr"]

#print(x)
#print(y)

X_train,X_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_prec=model.predict(X_test)

#error evaluation
print(mean_absolute_error(y_prec,y_test))
print(mean_squared_error(y_prec,y_test))
print(mean_squared_error(y_prec,y_test)**0.5)

#user input

area_sqft=float(input("Enter the sqrt"))
bedroom=float(input("Enter the bedroom"))
bathroom=float(input("Enter the bathroom"))
house_age=float(input("Enter the house age"))

house=pd.DataFrame(
    {
        "area_sqft":[area_sqft],
        "bedrooms":[bedroom],
        "bathrooms":[bathroom],
        "house_age_years":[house_age]
    })
print(round(model.predict(house)[0]))





