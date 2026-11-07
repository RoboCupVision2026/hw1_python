from pathlib import Path as pt
import random as rd

address = pt('img')
files = list(address.glob('*.png'))
picked = set()
while len(picked) < 50:
    order = rd.choice(files)
    picked.add(order)
for i in picked:
    new = i.with_suffix('.jpg')
    i.rename(new)
print('over')