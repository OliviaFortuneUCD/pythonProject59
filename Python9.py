import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


wine_data = pd.read_csv('winequality-red.csv')

X = wine_data['quality']
Y = wine_data['citric acid']

corr, _ = pearsonr(X, Y)
print('Pearsons correlation: %.3f' % corr)


 