import numpy as np
import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
print(wine_df.head())

wine_df.hist(bins=10,figsize=(15,12))
plt.show()

