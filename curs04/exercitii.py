a = input("Scrie primul numar: ") # Primul numar
b = input("Scrie al doilea numar: ") # Primul numar

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if a * b <= 1000:
        print(a * b)
    else:
        print(a + b)
else:
    print("NU AI SCRIS NUMERE")