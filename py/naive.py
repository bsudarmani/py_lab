'''import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

data = pd.read_csv("loanc.csv", sep=r"\s+")

print("Column Names:", data.columns.tolist())
print("Shape:", data.shape)
print(data.head())


X=data.drop("credit.policy",axis=1)
y=data["not.fully.paid"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=GaussianNB()

model.fit(X_train,y_train)

y_prec=model.prec(X_test)

print(accuracy_score(y_test,y_prec))

print(classification_report(y_test,y_prec))

plt.imshow(confusion_matrix(y_test,y_prec),cmap="Blues")
plt.title("Random Tree Classifier")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()
'''


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
data = pd.read_csv("loanc.csv")

X = data.drop("int.rate", axis=1)
y = data["not.fully.paid"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = GaussianNB()

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)

# Visualization
plt.imshow(confusion_matrix(y_test, y_pred), cmap="Blues")
plt.title("Naive Bayes Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()



