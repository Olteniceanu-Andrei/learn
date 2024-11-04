from shutil import which

# r -> citire, nu adauga, daca fisierul nu exista apare eroare
# w -> scriere, daca fisierul nu exista, il adauga. daca exista informatie deja scrisa in fisier, se rescrie informatia
# a -> scriere, daca exista informatie in fisier, nu se rescrie - se scrie in continuare adica
# r+ -> scrie, citeste, daca fisierul nu exista, apare eroare
fisier = open('nume_fisier.txt', 'w')
fisier.write("Salut frate")
fisier.close()

with open("nume_fisier.txt", "r") as file:
    text = file.readlines()
    print(text)