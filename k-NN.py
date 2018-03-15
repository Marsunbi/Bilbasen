import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import tensorflow as tf

df = pd.read_csv('final_dataset.csv', sep='\t', index_col=0)
df = df.drop(['Car'], 1)

X = np.array(df.drop(['Price'], 1))
y = np.array(df['Price'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

# Format:               [HK, 0-100, KM driven, KM/L, Year, Doors, Motor]
example_measure = np.array([[150.0, 8.0, 15, 22.0, 2017, 4.0, 2.0]])
prediction = clf.predict(example_measure)
prediction = prediction[0]
print("Projected price: " + str(prediction))


