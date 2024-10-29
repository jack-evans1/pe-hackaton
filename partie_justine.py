
import pandas as pd
pd.__version__
import matplotlib.pyplot as plt
import numpy as np
import IPython

df= pd.read_csv('pe-hackaton/data/happiness2022.csv')
#print(df.head(5))
#df = df_long.head(44)
df['écart entre positif et non negatif'] = 1-df['Negative affect']- df['Positive affect']
pays= df.groupby(['Country name'])

print("par pays" , pays.head(10))
pays_moy = pays.mean()


print("pays moyenné", pays_moy.head(10))

df.plot.scatter(x = 'Positive affect', y = 'Negative affect', by = 'Country name')
plt.plot([0,1],[1,0], color = 'Red')
#plt.tight_layout()
plt.show()