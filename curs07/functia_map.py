# Functia map are rolul de a modifica fiecare element al unei liste

lista = [1, 2, 3, 4, 5]

inmultire = lambda x: x * 2

rezultat = list(map(inmultire, lista))
print(rezultat)