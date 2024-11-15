# import pandas as pd
# import numpy as np
# import datetime
#
# lista = [10, 20, 30, 40, 50]
# etichete = ['a','b','c','d','e']
# serie = pd.Series(lista, index=etichete)
# print('====================')
# print(serie[serie > 19])
#
# data = {"Nume": ['Andrei','Marius','Radu'],
#         "Varsta": [14, 25, 30],
#         "Salariu": [0, 5000, 7500]}
# print('====================')
# df = pd.DataFrame(data)
# nume = df["Nume"]
# print(nume)
#
# salariu = df.at[1, "Salariu"]
# print('====================')
# print(salariu)
#
# df['Experienta'] = ['1 an', '2 ani', '3 ani']
# print('====================')
# print(df.iloc[2])
#
# df_filtrat = df[(df['Salariu'] > 3000) & (df['Varsta'] > 25)]
#
# print(df_filtrat)
#
# print('====================')
#
# df_sortat = df.sort_values(by="Varsta", ascending=False)
# print(df_sortat)

import pandas as pd

data = {"Nume": ["Andrei","Viorica","Andrei","George","Andrei"],
        "Varsta": [14, 21, 25, 50, 14],
        "Salariu": [0, 12000, 5000, 102000, 1]}

df = pd.DataFrame(data)

print(df)
print("============")

df_faraduplicates = df.drop_duplicates()

# drop_duplicates functioneaza doar daca toate valorile sunt egale

print(df_faraduplicates)

# Daca sunt valori cu None putem folosi .dropna .fillna

df["Experienta"] = [0, 5, 3 , 4 ,10]

print(df)

df.rename(columns={"Experienta": "Nr ani de munca"}, inplace=True)

print(df)
print("======================")

df.to_csv("date.csv", index=False)
print(df)