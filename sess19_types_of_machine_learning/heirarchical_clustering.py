# Python file to demonstrate heirarchical clustering algorithm

# Import the required module
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# Generate a synthetic customer dataset with income and spending score
data = {
    'Income' : np.random.randint(20000,100000,50),
    'Spending Score' : np.random.randint(1,50,50)
}

# Create a Dataframe and display the first 10 rows
df = pd.DataFrame(data)
print(f"The first 10 rows of the customer income and spending score are:\n{df[:10]}")

# Visualise the entire datasset
plt.figure(figsize=(10,8))
plt.scatter(df['Income'],df['Spending Score'])
plt.title('Sythetic Dataset: Income vs Spending Score')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.show()

# Create a dendrogram
plt.figure(figsize=(10,8))
dendrogram = sch.dendrogram(sch.linkage(df, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Euclidean Distances')
plt.show()

# Apply Agglomerative Clustering
hc = AgglomerativeClustering(n_clusters=3,metric='euclidean',linkage='ward')
df['Cluster'] = hc.fit_predict(df)

# Plot the Clusters
plt.figure(figsize=(10,6))
plt.scatter(df['Income'],df['Spending Score'],c=df['Cluster'],cmap='viridis')
plt.title("Heirarchical Clustering: Income vs Spending Score")
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.show()