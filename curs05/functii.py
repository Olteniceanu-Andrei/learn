# print("Ana")
# Mai multe detalii despre built-in functions:  https://docs.python.org/3/library/functions.html
# control + b sa vedem detalii despre functie

# def functia_mea(param1, param2):
#     return "ok"
#
# rezultat = functia_mea(1, 2)
# print(rezultat)
#fara print in functie -> de folosit return

# def suma(a: int, b: int) -> int:       definim tipul parametrilor de intrare adica a si b int si de iesire din functie tot int
#     return a + b
#
# rezultat = suma(10,20)
# print(type(rezultat))

# def rezultat(a: int,b: int) -> (int, int):#pentru fiecare element din return ( in cazul nostru sunt 2 , trebuie sa definim parametrii de iesire de asta am pus in paranteza int, int)
#     return a + b, a - b
#
# rezultat_suma , rezultat_diferenta = rezultat(10, 3)
# # deoarece avem doua elemente in return, putem sa le incorporam in doua variabile diferite precum mai sus
# print(rezultat_suma)
# print(rezultat_diferenta)

def rezultat(a: int = 3, b: int = 2, c:int = 1, *args, **kwargs):
    suma = a + b + c
    print(args)
    print(args[2])
    print(kwargs['d'])
    for i in args:
        suma = suma + i
    return suma

#*args primeste cate elemente se apeleaza in functie si este de tip tupple
#**kwargs este de tip dictionar
salut = rezultat(1, 2, 3, 1, 2 ,3 ,4, d=3, e=4, f=5)

print(salut)