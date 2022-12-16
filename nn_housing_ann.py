from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout


housing = fetch_california_housing(as_frame=True)

X = housing['data']
y = housing['target']

X = MinMaxScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.7)

model = Sequential()
model.add(Dense(16, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_absolute_percentage_error')

model.fit(X_train, y_train, batch_size=32, epochs=1)

loss = model.evaluate(X_test, y_test)

print(f'Loss (mean percentage error): {loss:.2f}')
