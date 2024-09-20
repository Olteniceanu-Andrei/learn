x = int(input("""
Selectati o valoare din lista:

1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi 

"""))

if x == 1:
    print("Afisare lista de cumparaturi")
elif x == 2:
    print("Adaugare element")
elif x == 3:
    print("Stergere element")
elif x == 4:
    print("Sterere lista de cumparaturi")
elif x == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")