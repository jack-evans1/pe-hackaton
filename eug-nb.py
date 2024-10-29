# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

df = pd.read_csv('data/happiness2022.csv')
df.columns

# %%
df.describe()

# %%
df.plot()

# %%
df1 = df.groupby(by='year')
df2022 = df1.get_group(2022)
#df2 = df2.drop(columns ='year')
df2022['Healthy life expectancy at birth'].plot(c='red')
df2022[['Life Ladder', 'Log GDP per capita']].plot()
df2022[['Freedom to make life choices','Positive affect','Negative affect']].plot(title='liberté de choix')
df2022[['Generosity','Positive affect','Negative affect']].plot(title='générosité')
df2022[['Perceptions of corruption','Positive affect','Negative affect']].plot(title='corruption')
df2022[['Social support','Positive affect','Negative affect']].plot(title='support social')

# %%
df2022.hist()

# %%
# on va essayer de comparer les histogrammes de 2022 avec ceux des années précédentes, pour regarder si la répartition varie

df2005=df1.get_group(2005)
df2005.hist()

# %%
#on remarque que les effectifs cumulés sont faibles (odg<50) => il n'y a pas assez de données sur les premières années
#on va donc étudier une autre année

df2010=df1.get_group(2010)
df2010.hist()

# %%
# j'ai envie de voir l'évolution du nb de pays participant à l'étude en fonction du temps
# je considère qu'un pays participe à partir du moment où il possède une ligne avec le nom de l'année 
df2 = df[['Country name','year']]
df3 = df2.groupby(by='year')
df3.size().plot(title='Nombre de pays participants')

# %%
# on remarque effectivement que peu de pays participent au début de l'étude (en 2005)
# on veut maintenant étudier la cohérence des données

# %%
# cette échelle ne convient pas, on sélectionne les données ayant les mêmes ordres de grandeur

# %%
df5 = df['Healthy life expectancy at birth'].to_frame()
df5.boxplot()

# %%
df6 = df[['Life Ladder', 'Log GDP per capita']]
df6.boxplot()

# %%
#ici on a peu d'outlier, le set est fiable
df7 = df[['Freedom to make life choices','Generosity','Perceptions of corruption','Social support','Positive affect','Negative affect']]
df7.boxplot()

# %%
# là on a beaucoup plus de données extrêmes
