import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd


df = pd.read_csv('C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/test.csv', sep='\t', index_col=0)
df = df.drop(['Car'], 1)

X = np.array(df.drop(['Price'], 1))
y = np.array(df['Price'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measure = np.array([[100.0, 100, 27.0, 11.0, 2013, 5.0, 1.8]])
prediction = clf.predict(example_measure)
print(prediction)
