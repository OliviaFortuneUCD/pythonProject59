import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

wine_df = pd.read_csv('winequality-red.csv')

#create an extra column called quality
categor_condn=[ (wine_df['quality']>=7),
               (wine_df['quality']<=4)]
rating=['superior','inferior']
wine_df['rating'] = np.select(categor_condn,rating,default='fine')



fig = px.scatter(wine_df, x="volatile acidity", y="alcohol", color="rating",
                 facet_col="rating", title="Alcohol, Volatile Alcohol Vs Rating")

fig.update_xaxes(showgrid=False)

fig.show()
