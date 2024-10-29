import numpy as np
import pandas as pd

#### on créée une liste des colonnes manquantes par pays et par année 

df = pd.read_csv('data/happiness2022.csv')
print(df.shape)

def valeurs_manquantes(df):
    # ON ajoute les colonnes 'valeur manquante' et 'statut'
    df['valeur manquante'] = df.isna().sum(axis=1)
    df['statut'] = pd.cut(df["valeur manquante"], bins=[-1, 0, 200], labels=['ok', 'missing'])

    # On groupe par année
    df_by_year = df.groupby(by='year')
    missing = dict()

    for group, subdf in df_by_year:
        # On initialise la liste pour les pays avec données manquantes pour chaque groupe
        missing[group] = []

        # ON récupère les pays ayant le statut 'missing'
        for _, row in subdf[subdf['statut'] == 'missing'].iterrows():
            country = row['Country name']
            missing_columns = row[row.isna()].index.tolist()  # Colonnes avec des valeurs manquantes
            missing[group].append([country, missing_columns])

        print(f"Année {group} : {missing[group]}")

valeurs_manquantes(df)
