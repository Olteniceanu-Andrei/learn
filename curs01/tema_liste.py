lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

ascendent = sorted(lista)
print(sorted(lista)) #am incercat cu .sort si sa incorporez noua lista intr-o noua lista doar ca .sort() face modificari doar pe lista unde este executat
descendent = list(sorted(lista).__reversed__()) # ca si in cazul cu .sort , .reverse are acelasi behaviour. Am folosit versiunile reversed si sorted pentru a pastra aceeasi valoare a listei.

print(descendent)

print(ascendent[1::2])
print(ascendent[::2])
print(ascendent[2::3])