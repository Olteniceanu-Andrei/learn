lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

n = 3

a = len(lista_start)
lista1 = []
for i in range(a):
    if i % n == 0:
        lista1.append(lista_start[i])

print(lista_noua)
