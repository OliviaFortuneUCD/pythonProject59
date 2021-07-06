import pandas
from sklearn import linear_model
df = pandas.read_csv("carsclean.csv")
missing = df.isnull
print(missing)
df[['Weight', 'CO2']] = df[['Weight', 'CO2']].fillna(0)
print(df)