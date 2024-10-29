import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/happiness2022.csv')
print(df.head())
print(df.columns, df['Country name'].unique())

