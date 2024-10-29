
import pandas as pd
pd.__version__
import matplotlib.pyplot as plt
import numpy as np
import IPython

df= pd.read_csv('pe-hackaton/data/happiness2022.csv')
#Je voulais regarder si l'écart entre positif et non-négatif (d'où le 1-Negative affect) par pays était bien nulle
df['écart entre positif et non negatif'] = 1-df['Negative affect']- df['Positive affect']

by_pays= df.groupby(['Country name'])

#ce fut un échec
country=df['Country name'].unique()
plt.figure()
#j'ai essayé plutôt de tracer un nuage de point positif en fonction de négatif par pays et de regarder où ces nuages se situent par rapport à la droite y = 1-x 
for pays in country :
    by_pays.get_group(pays).plot.scatter(x = 'Positive affect', y = ['Negative affect'])
plt.plot([0,1],[1,0], color = 'Red')
plt.tight_layout()
plt.show()
#problème il m'affiche les figures de chaque pays séparemment donc 166 figures...