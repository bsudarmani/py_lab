from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

iris=load_iris()
x=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=42
)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

print("Accuracy_score")
print(accuracy_score(y_test,y_pred)*100)

print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))

print("classification report")
print(classification_report(y_test,y_pred))

plt.plot(y_test)
plt.plot(y_pred)
plt.title("Test vs flower")
plt.xlabel("Test Samples")
plt.ylabel("Flower Samples")
#plt.legend()
plt.show()


