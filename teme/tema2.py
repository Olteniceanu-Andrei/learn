a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = 0
lista = []

while a[x] in b:
    if a[x] not in lista:
        lista.append(a[x])
        x = x + 1
    else:
        x = x + 1

print(lista)