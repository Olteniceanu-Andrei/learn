x = input("Nume: ")

if type(x) == str:
    print(f"Sirul de caractere a fost gasit de {x}")
elif type(x) == int:
    print(f"Sirul {x} este de tip int")
else:
    print("Sirul introdus nu este de tip str sau int")