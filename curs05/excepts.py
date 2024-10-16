# exceptii
# codul care credem ca va avea eroare il bagam in try
# Exception cuprinde exceptiile standar din python
# de ex se foloseste doar exceptia mica nu tot Exception: ValueError in cazul nostru

# Structura lui try:


# text = input("Adauga un nr: ")
# try:                                         <- in aceasta sectiune punem codul pe care vrem sa il rulam
#     conversie = int(text)
# except Exception:                            <- in aceasta sectiune mentionam ce tip de eroare vrem sa exceptam.
#     print("Avem o exceptie")                    Practic anuntam ce eroare sa nu o afiseze in terminal si sa treaca peste
# else:                                        <- in caz ca nu avem nici o exceptie in urma rularii codului, trecem
#     print(conversie)                            si executam ce gasim in sectiunea else
# finally:                                     <- indiferent daca avem eroare sau nu, cand folosim finally executam
#     print("Se executa oricand")                 intotdeauna la final de cod ce avem in aceasta sectiune