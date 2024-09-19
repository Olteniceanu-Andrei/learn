def suma(q):
    if q == 0:
        return q
    return q + suma(q-1)

print(suma(10))

print(dir(__builtins__))

def adunare(a, b):
    sum = int(a) + int(b)
    print(sum)

adunare(input("Primul numar"), input("Al doilea numar"))

def lista(mylist):
    mylist.append(4)

listuta = [1,2,3]

lista(listuta)

print(listuta)

def parametrii(a, b, **kwargs):
    print(f"{a} + {b} + {kwargs}")

parametrii(2, 3, z=10, y=30, c="Salut")


