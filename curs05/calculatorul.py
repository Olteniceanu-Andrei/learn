# 2 valori introduse de la tastatura si operatia
# asta inseamna 3 inputuri

def validare_nr(nr):
    numar = input(f"Numarul {nr} este: ")
    while numar.isdigit() is False:
        numar = input(f"Numarul {nr} este: ")
    return int(numar)

def validare_operand(operand):
    while operand not in "+-*/":
        operand = input("Valoare gresita, scrie un operator valid: ")
    return operand

def suma(operator1: int, operator2: int):
    return operator1+operator2

def dif(operator1: int, operator2: int):
    return operator1-operator2

def inmultire(operator1: int, operator2: int):
    return operator1*operator2

def impartire(operator1: int, operator2: int):
    while operator2 == 0:
        operator2 = int(input("Scrie un numar diferit de 0: "))
    return operator1/operator2

def principal():
    op1 = validare_nr(1)
    op2 = validare_nr(2)
    operand = input("Scrie operator: ")
    rezultat_ope = validare_operand(operand)

    if rezultat_ope == "+":
        a = suma(op1, op2)
    elif rezultat_ope == "-":
        a = dif(op1, op2)
    elif rezultat_ope == "*":
        a = inmultire(op1, op2)
    elif rezultat_ope == "/":
        a = impartire(op1, op2)

    return a

print(principal())