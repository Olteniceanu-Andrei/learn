persoane = [
{
 'nume': 'George',
 'filme': ['Shrek', 'Bond', 'Fight Club']},
{
 'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
{
 'nume' : 'Stefan',
 'filme': ['Fight Club', 'Slumdog Milionare']}
]

vizionatmax = 0
utilizatormax = None   # Utilizatorul cu cele mai multe filme vizionate

for utilizator in persoane:
    vizionate = len(utilizator['filme'])
    if vizionate > vizionatmax:
       vizionatmax = vizionate
       utilizatormax = utilizator['nume']

print(f"{utilizatormax} a vazut de {vizionatmax}")
