import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
wine_df = pd.read_csv('winequality-red.csv')
print(wine_df.head())

plt.figure(figsize=(10,5))
correlation = wine_df.corr()
sns.heatmap(correlation,annot=True,cmap='viridis')