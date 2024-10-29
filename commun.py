import numpy as np
import pandas as pd

df = pd.read_csv('data/happiness2022.csv')
print(df.head())
print(df.columns, df['Country name'].unique())

