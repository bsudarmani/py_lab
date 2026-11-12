
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Dataset
data = pd.read_csv("Mall_Customers.csv")

X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Create Model
model = KMeans(n_clusters=5, random_state=42, n_init=10)

# Clustering
y_pred = model.fit_predict(X)

# Display Clusters
print("Cluster Labels:")
print(y_pred)

# Visualization
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_pred, cmap="rainbow")
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            color="black", marker="X", s=150)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()
