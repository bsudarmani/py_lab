
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and Train Model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred), "%")

# Visualization 1: Confusion Matrix
plt.imshow(confusion_matrix(y_test, y_pred), cmap="Blues")
plt.title("KNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()

# Visualization 2: Actual vs Predicted
plt.plot(y_test, label="Actual")
plt.plot(y_pred, label="Predicted")
plt.title("Actual vs Predicted")
plt.xlabel("Test Samples")
plt.ylabel("Flower Class")
plt.legend()
plt.show()


===========================================


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.ensemble import ExtraTreesClassifier

# Load Dataset
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# Create Model
model = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Train Model
model.fit(X, y)

# Feature Importance
importance = model.feature_importances_

# Display Features
print("Feature Importance:")
print(importance)

# Visualization
plt.bar(X.columns, importance)
plt.xticks(rotation=90)
plt.title("Extra Trees Feature Selection")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

================================================

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = [[1000], [1200], [1500], [1800], [2000]]
y = [20, 25, 30, 36, 40]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Prediction
pred = model.predict([[1600]])

print("Predicted House Price:", pred[0], "Lakhs")

# Visualization
plt.scatter(X, y, label="Actual")
plt.plot(X, model.predict(X), label="Predicted")
plt.title("House Price Prediction")
plt.xlabel("House Size")
plt.ylabel("Price (Lakhs)")
plt.legend()
plt.show()



=====================================================



import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create Model
model = SVC(kernel="linear")

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)

# Visualization
plt.imshow(confusion_matrix(y_test, y_pred), cmap="Blues")
plt.title("SVM Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()




=====================================================


import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Dataset
data = pd.read_csv("college_elective_selection_dataset.csv")

print(data.head())

# Input Features
X = data[["department", "year_of_study", "gender"]]

# Output Target
y = data["elective_course"]

# Convert categorical data into numerical data
X = pd.get_dummies(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Visualization
plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("College Elective Decision Tree")
plt.show()

# User Input
department = input("Enter Department (MCA/BCA/B.Sc CS/M.Sc CS): ")
year = int(input("Enter Year of Study (2 or 3): "))
gender = input("Enter Gender (Male/Female/Prefer not to say): ")

# Create Input DataFrame
new_student = pd.DataFrame({
    "department": [department],
    "year_of_study": [year],
    "gender": [gender]
})

# Convert categorical data
new_student = pd.get_dummies(new_student)
new_student = new_student.reindex(columns=X.columns, fill_value=0)

# Predict Elective
prediction = model.predict(new_student)

print("Predicted Elective Course:", prediction[0])

===================================================================


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
data = pd.read_csv("customer_churn.csv")

X = data.drop("Churn", axis=1)
y = data["Churn"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)

# Visualization
plt.imshow(confusion_matrix(y_test, y_pred), cmap="Blues")
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()

======================================================================
