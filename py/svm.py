from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data=load_breast_cancer()
x=data.data
y=data.target

X_train,X_test,y_train,y_test=train_test_split(
  x,y,test_size=0.2,random_state=42
    )

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model=SVC(kernel="linear")
model.fit(X_train,y_train)
y_prec=model.predict(X_test)


print("Accuracy Score")
print(accuracy_score(y_test,y_prec))

plt.imshow(confusion_matrix(y_test,y_prec),cmap="Blues")
plt.xlabel("Preicted")
plt.ylabel("Accuracy")
plt.title("SVM Confusion Matrix")
plt.colorbar()
plt.show()
