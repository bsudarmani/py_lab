import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

data=pd.read_csv("elective.csv")
#print(data.head(5))

X=data[["gender","department","year_of_study"]]
y=data["elective_course"]


X=pd.get_dummies(X)
print(X)
print(y)

X_train,X_test,y_train,y_test=train_test_split(
 X,y,test_size=0.2,random_state=42,
)

model=DecisionTreeClassifier(random_state=42)

model.fit(X_train,y_train)

y_prec=model.predict(X_test)

print("Accuracy")
print(accuracy_score(y_test,y_prec)*100)

print("Confusion Matrix")
print(confusion_matrix(y_test,y_prec))

print("classification Report")
print(classification_report(y_test,y_prec,zero_division=0))

plt.figure(figsize=(20,10))
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


gender=input("Enter the gender")
department=input("Enter the department")
year_of_study=int(input("Enter the year"))
new_student=pd.DataFrame(
    {
        gender:["gender"],
        department:["department"],
        year_of_study:["year_of_study"]
    })

new_student=pd.get_dummies(new_student)
new_student=new_student.reindex(columns=X.columns,fill_value=0)
prediction=model.predict(new_student)

print(prediction[0])
