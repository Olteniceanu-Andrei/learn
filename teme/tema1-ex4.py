x = int(input("Introduceti un numar: "))

if x > 0 and x < 10:
    print(f"Numarul {x} este pozitiv si mai mic decat 10")
elif x == 0:
    print(f"Numarul este 0")
elif x < 0:
    x = x * -1
    print(x)
