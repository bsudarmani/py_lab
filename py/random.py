import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pandas as pd

data=pd.read_csv("churn1.csv")

print(data.head(5))
print(data.shape)

X=data.drop("Churn",axis=1)
y=data["Churn"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,y_train)

y_prec=model.predict(X_test)

print(accuracy_score(y_test,y_prec))

print(classification_report(y_test,y_prec))

plt.imshow(confusion_matrix(y_test,y_prec),cmap="Blues")
plt.title("RanomForest classifier")
plt.xlabel("Prediction")
plt.ylabel("Actual")
plt.colorbar()
plt.show()
