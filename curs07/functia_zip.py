# Primeste doua sau mai multe structuri iterabile si returneaza un iterabil de tip zim format din tupluri
# alcatuit din structuri initiale

lista_nr = [1, 2, 3, 4, 5]
lista_strings = ("unu", "doi", "trei", "patru", "cinci")

lista = list(zip(lista_nr, lista_strings))

print(lista)