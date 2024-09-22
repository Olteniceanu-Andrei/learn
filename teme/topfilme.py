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

print(f"{utilizatormax} a vazut {vizionatmax} filme")

a = 0 # Filmul Shrek
b = 0 # Filmul Bond
c = 0 # Filmul Fight Club
d = 0 # Filmul The Nun
e = 0 # Filmul Dracula
f = 0 # Filmul Slumdog Milionare

for vizionate in persoane:
    if 'Shrek' in vizionate['filme']:
        a += 1
    if 'Bond' in vizionate['filme']:
        b += 1
    if 'Fight Club' in vizionate['filme']:
        c += 1
    if 'The Nun' in vizionate['filme']:
        d += 1
    if 'Dracula' in vizionate['filme']:
        e += 1
    if 'Slumdog Milionare' in vizionate['filme']:
        f += 1

if a > b and a > c and a > d and a > e and a > f:
    print(f"Cel mai vizionat film a fost Shrek de {a} ori")
if b > a and b > c and b > d and b > e and b > f:
    print(f"Cel mai vizionat film a fost Bond de {b} ori")
if c > b and c > a and c > d and c > e and c > f:
    print(f"Cel mai vizionat film a fost Fight Club de {c} ori")
if d > b and d > c and d > a and d > e and d > f:
    print(f"Cel mai vizionat film a fost The Nun de {d} ori")
if e > b and e > c and e > d and e > a and e > f:
    print(f"Cel mai vizionat film a fost Dracula de {e} ori")
if f > b and f > c and f > d and f > e and f > a:
    print(f"Cel mai vizionat film a fost Slumdog Milionare de {f} ori")