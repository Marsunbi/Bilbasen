import pandas as pd
import re as re
import numpy as np
import matplotlib.pyplot as plt

file = "C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/bilbasen3 - dont delete.csv"
data = pd.read_csv(file, header=None, sep=";")
cars_df = pd.DataFrame(data)

column_names = ['Car', 'HK', 'KM driven', 'KM/L', '0-100', 'Price', 'Year']
cars_df.columns = column_names

cars_df['Doors'] = cars_df['Car'].all()[-2:]
cars_df.Doors = cars_df.Doors.all()[:-1]
cars_df.Doors = pd.to_numeric(cars_df.Doors)

cars_df['HK'] = cars_df['HK'].map(lambda x: str(x)[:-3])
cars_df['HK'] = pd.to_numeric(cars_df['HK'])

cars_df['KM/L'] = cars_df['KM/L'].map(lambda x: x.replace(',', '.'))
cars_df['KM/L'] = cars_df['KM/L'].map(lambda x: str(x)[:-4])
cars_df['KM/L'] = pd.to_numeric(cars_df['KM/L'])

cars_df['0-100'] = cars_df['0-100'].map(lambda x: x.replace(',', '.'))
cars_df['0-100'] = cars_df['0-100'].map(lambda x: str(x)[:-5])
cars_df['0-100'] = pd.to_numeric(cars_df['0-100'])

cars_df['Price'] = cars_df['Price'].map(lambda x: x.replace('.', ''))
cars_df['Price'] = cars_df['Price'].map(lambda x: str(x)[:-4])
cars_df['Price'] = pd.to_numeric(cars_df['Price'])

cars_df['Car'] = cars_df.Car.map(lambda x: x.replace(',', '.'))
cars_df['Motor'] = cars_df.Car.map(lambda x: re.findall("\d\.\d", x))
cars_df['Motor'] = cars_df.Motor.map(lambda x: [float(i) for i in x])

#cars_df['Motor'] = cars_df.Motor.apply(pd.to_numeric)
#cars_df['Motor'] = pd.to_numeric(cars_df['Motor'])
#cars_df['Motor'].convert_objects(convert_numeric=True)

cars_df['Car'] = cars_df.Car.map(lambda x: re.findall("\w*\s\w*", x)[0])


print(cars_df.head())
print(type(cars_df['Car'][0]))
print(type(cars_df['Motor'][0]))
