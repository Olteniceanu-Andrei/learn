# Functie anonima care indeplineste o singura functiune

suma = lambda x, y: x + y

rezultat = suma(3,4)
print(rezultat)

lista = [{
    "nume": "Andrei",
    "varsta": 15
},
{
    "nume": "Marian",
    "varsta": 5
},
{
    "nume": "George",
    "varsta": 30
}
]

sortare = sorted(lista, key= lambda numar: numar['varsta'], reverse=True)
print(sortare)