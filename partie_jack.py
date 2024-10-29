import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/happiness2022.csv')

def presentation(df): #donnees de base du dataframe
    print('Taille : ', df.shape)
    print('Colonnes: ', df.columns)
    print('Pays : ', df['Country name'].unique().size)
    print('Annees : ', np.sort(df['year'].unique()))

#presentation(df)

#######################################TRACES DE GRAPHES




#Esperance de vie au  cours du temps:

def donnees_pays(pays,df): #cree un df de groupby selon un pays
    groups = df.groupby(by = 'Country name')
    dico = dict(list(groups))
    return dico[pays]




def trace_esp_pays(pays, df): #trace un graphe de l'evolution de l'esperence de vie dans une liste de pays
    fig = plt.figure()

    for pays in pays:
        plt.plot(donnees_pays(pays,df)['year'], donnees_pays(pays,df)['Healthy life expectancy at birth'], label = pays, linestyle='-', marker='o')

    plt.legend()
    plt.show()




pays_interessants = ['France', 'United States', 'Russia', 'Brazil', 'China', 'Egypt']

trace_esp_pays(pays_interessants, df)


