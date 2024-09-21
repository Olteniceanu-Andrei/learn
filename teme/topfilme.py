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
    vizionate = len(persoane['filme'])
    if vizionate > vizionatmax:
        vizionate = vizionatmax
        utilizatormax = persoane['filme']

print(f"A vazut de {vizionatmax}")
