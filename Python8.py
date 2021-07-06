import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

wine_df = pd.read_csv('winequality-red.csv')



sns.countplot(wine_df['quality'])
wine_df['quality'].value_counts()