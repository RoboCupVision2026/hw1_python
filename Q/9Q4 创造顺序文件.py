from pathlib import Path
import random as rd

letter = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
total = 100

wj = Path('img')
wj.mkdir(exist_ok = True)
used = set()

while len(used) < total:
    name = ''.join(rd.choices(letter,k=4))
    if name not in used:
        path_a = wj/f'{name}.png'
        path_a.touch()
        used.add(name)
print('over')