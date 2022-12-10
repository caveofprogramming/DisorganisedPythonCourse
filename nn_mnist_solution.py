"""
Build a neural network to recognise digits in the MNIST dataset.
Display a chart showing only digits that were NOT recognised correctly.
"""

from keras.datasets import mnist
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import accuracy_score
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(500, input_dim=len(X_train[0]), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(len(y_train[0]), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

model.fit(X_train, y_train, epochs=20, batch_size=256)

#y_predicted = model.predict(X_test)

loss, accuracy = model.evaluate(X_test, y_test, batch_size=256)

print(f"Accuracy: {accuracy:.2f}")
