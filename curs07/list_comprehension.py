numbers_list = []
for x in range(30):
    if x % 2 == 0:
        numbers_list.append(x)

print(numbers_list)

numere_lista = [x for x in range(30) if x % 2 == 0]
print(numere_lista)