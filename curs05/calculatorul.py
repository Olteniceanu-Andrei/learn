# 2 valori introduse de la tastatura si operatia
# asta inseamna 3 inputuri

def validare_nr(nr):
    numar = input(f"Numarul {nr} este: ")
    while numar.isdigit() is False:
        numar = input(f"Numarul {nr} este: ")
    return int(numar)

def validare_operand(operand):
    operand = input("Scrie operator: ")
    while operand not in "+-*/":
        operand = input("Valoare gresita, scrie un operator valid: ")
    return operand

def suma(operator1: int, operator2: int):
    return operator1+operator2

def dif(operator1: int, operator2: int):
    return operator1-operator2


operator1 = validare_nr(1)
operator2 = validare_nr(2)

print(operator1, operator2)

rezultat_ope = validare_operand("da")

print(rezultat_ope)

a = suma(operator1, operator2)
b = dif(operator1, operator2)
print(a)
print(b)