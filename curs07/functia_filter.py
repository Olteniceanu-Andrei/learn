# Filtreaza elementele dintr-un iterabil

lista = [1, 2, 3, 4, 5]

lista2 = list(filter(lambda x: x%2 == 0, lista))

print(lista2)