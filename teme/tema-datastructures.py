lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

sortata = lista.copy()
sortata.sort()
print(sortata)
sortata.reverse()
print(sortata)
sortata.reverse()

print(f" Numerele pare din lista sunt {sortata[1::2]}")
print(f" Numerele impare din lista sunt {sortata[0::2]}")
print(f" Numerele multipli ai lui 3 din lista sunt {sortata[2::3]}")