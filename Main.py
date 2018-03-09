import pandas as pd
import re as re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file = "C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/bilbasen3 - dont delete.csv"
data = pd.read_csv(file, header=None, sep=";")
cars_df = pd.DataFrame(data)

column_names = ['Car', 'HK', 'KM driven', 'KM/L', '0-100', 'Price', 'Year']
cars_df.columns = column_names

cars_df['Doors'] = cars_df.Car.apply(lambda x: x[-2:])
cars_df['Doors'] = cars_df.Doors.apply(lambda x: x[:-1])
cars_df.Doors = pd.to_numeric(cars_df.Doors, errors='coerce')

#Should be converted to int
cars_df['HK'] = cars_df['HK'].map(lambda x: str(x)[:-3])
cars_df['HK'] = pd.to_numeric(cars_df['HK'])
#cars_df['HK'] = cars_df['HK'].astype('int64')

cars_df['KM driven'] = pd.to_numeric(cars_df['KM driven'])
cars_df['KM driven'] = cars_df['KM driven'].astype(int)

cars_df['KM/L'] = cars_df['KM/L'].map(lambda x: x.replace(',', '.'))
cars_df['KM/L'] = cars_df['KM/L'].map(lambda x: x[:-4])
cars_df['KM/L'] = pd.to_numeric(cars_df['KM/L'])
mean_value = cars_df['KM/L'].mean()
cars_df['KM/L'] = cars_df['KM/L'].fillna(mean_value)

cars_df['0-100'] = cars_df['0-100'].map(lambda x: x.replace(',', '.'))
cars_df['0-100'] = cars_df['0-100'].map(lambda x: x[:-5])
cars_df['0-100'] = pd.to_numeric(cars_df['0-100'])
mean_value = cars_df['0-100'].mean()
cars_df['0-100'] = cars_df['0-100'].fillna(mean_value)

cars_df['Price'] = cars_df['Price'].map(lambda x: x.replace('.', ''))
cars_df['Price'] = cars_df['Price'].map(lambda x: x[:-3])
cars_df['Price'] = pd.to_numeric(cars_df['Price'], errors='coerce')
cars_df = cars_df.dropna(axis=0, how='any')
cars_df['Price'] = cars_df['Price'].astype('int64')

cars_df['Car'] = cars_df.Car.map(lambda x: x.replace(',', '.'))
cars_df['Motor'] = cars_df.Car.apply(lambda x: np.nan if re.search("\d\.\d", x) is None else re.search("\d\.\d", x).group(0))
cars_df['Motor'] = pd.to_numeric(cars_df['Motor'])
mean_value = cars_df['Motor'].mean()
cars_df['Motor'] = cars_df['Motor'].fillna(mean_value)

cars_df['Car'] = cars_df.Car.map(lambda x: re.findall("\w*\s\w*", x)[0])

#Set the car column as index
#cars_df = cars_df.set_index('Car')

cars_df.to_csv('test.csv', sep='\t')

print(cars_df.head())
print(cars_df.info())

corr = cars_df.corr()

#sns.heatmap(corr, annot=True)
#plt.show()

#sns.pairplot(cars_df, hue='Price')

