import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = {
    'one': [98, 99, 100, 101, 102],
    'two': [60, 80, 100, 120, 140],
}

print(np.mean(data['one']))
print(np.mean(data['two']))
print(np.var(data['one']))
print(np.var(data['two']))

df = pd.DataFrame(data)
print(df)

scaler = StandardScaler()

X = scaler.fit_transform(df)

print(np.mean(X[:,0]))
print(np.var(X[:,0]))
print(np.mean(X[:,1]))
print(np.var(X[:,1]))