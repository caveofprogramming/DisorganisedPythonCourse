"""
Load the iris data.

Fit a k-means model to the data (3 clusters)

Use the predict method of the model to predict the clusters

Plot the predicted clusters side-by-side with the actual clusters

Can you use an r squared score to compare the predicted with the actual clusters?
If not, why not?
"""

import sklearn.datasets as ds
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

data = ds.load_iris(as_frame=True)

target = data['target']
target_names = data['target_names']

df = data['data']
df['species_index'] = target
df['species'] = target.map(lambda n: target_names[n])

X = df.iloc[:,0:4]
X = StandardScaler().fit_transform(X)

model = KMeans(n_clusters=3)
model.fit(X)

predicted_target = model.predict(X)

x_label = df.columns[2]
y_label = df.columns[3]
x = df[x_label]
y = df[y_label]

fig = plt.figure(figsize=(16,9))

ax = fig.add_subplot(121)
ax.set_title("True Clusters")
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.scatter(x, y, c=target, cmap="plasma")

ax = fig.add_subplot(122)
ax.set_title("Predicted Clusters")
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.scatter(x, y, c=predicted_target, cmap="plasma")

plt.show()

pd.set_option("display.max_rows", 150)
df_clusters = pd.DataFrame()
df_clusters['True'] = target
df_clusters['Predicted'] = predicted_target

print(df_clusters)
