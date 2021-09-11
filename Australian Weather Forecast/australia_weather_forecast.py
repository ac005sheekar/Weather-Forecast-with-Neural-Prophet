# -*- coding: utf-8 -*-
"""Australia Weather Forecast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HithRRNZXlXHXix9GjO_py0vZX0qV-A-
"""

#The entire code written, documented and improvised by
#Sheekar Banerjee, A.I. Research Engineer, Cisscom LLC, USA
!pip install pandas

!pip install neuralprophet

#importing necessary libraries
import pandas as pd
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt
import pickle

#reading the CSV file dataset with pandas
df = pd.read_csv('weather Australia.csv')
df.head()

df.Location.unique()

df.columns

df.dtypes

melb = df[df['Location']=='Melbourne']
melb['Date'] = pd.to_datetime(melb['Date'])
melb.head()

plt.plot(melb['Date'], melb['Temp3pm'])
plt.show()

melb['Year'] = melb['Date'].apply(lambda x: x.year)
melb = melb[melb['Year']<=2015]
plt.plot(melb['Date'], melb['Temp3pm'])
plt.show()

data = melb[['Date', 'Temp3pm']] 
data.dropna(inplace=True)
data.columns = ['ds', 'y'] 
data.head()

#Train the Model
m = NeuralProphet()

model = m.fit(data, freq='D', epochs=1000)

#Forecasting the values
future = m.make_future_dataframe(data, periods=900)
forecast = m.predict(future)
forecast.head()

#Plotting the forcasting values
plot1 = m.plot(forecast)

plt2 = m.plot_components(forecast)

#Saving the model as .pkl (Pickle) file
with open('saved_model.pkl', "wb") as f:
    pickle.dump(m, f)

del m

with open('saved_model.pkl', "rb") as f:
    m = pickle.load(f)

future = m.make_future_dataframe(data, periods=900)
forecast = m.predict(future)
forecast.head()

plot1 = m.plot(forecast)

