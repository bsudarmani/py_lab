import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_wine
import pandas as pd
wine=load_wine()

x=pd.DataFrame(wine.data,columns=wine.feature_names)
y=wine.target

#print(x)
#print(y)

model=ExtraTreesClassifier(n_estimators=100,random_state=42)

#print(model)

model.fit(x,y)

feature_selection=model.feature_importances_

print(feature_selection)

plt.bar(x.columns,feature_selection)
plt.title("Feature Importance Prediction")
plt.xticks(rotation=90)
plt.xlabel("feature")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

