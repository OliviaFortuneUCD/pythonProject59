import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
Y = df['CO2']
regr = linear_model.LinearRegression()
Z = regr.fit(X, Y)
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)

#We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.

#We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.

#Which shows that the coefficient of 0.00755095 is correct:

#107.2087328 + (1000 * 0.00755095) = 114.75968

