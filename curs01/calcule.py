print("Acesta este un calculator")

z = input("Ce doresti sa calculezi? Pentru scadere scrie x, pentru adunare scrie y ")

if z == "x": # Adunare
    a = int(input("Scrie primul numar "))
    b = int(input("Scrie al doilea numar "))
    c = a + b
    print(f"{a} + {b} = {c}")
elif z == "y": #Scadere
    a = int(input("Scrie primul numar "))
    b = int(input("Scrie al doilea numar "))
    c = a - b
    print(f"{a} - {b} = {c}")
else:
    print("Program intrerupt, nu ai ales x sau y")