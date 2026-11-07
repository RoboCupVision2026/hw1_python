import os
import random
if not os.path.exists("img"):
    os.mkdir("img")
chars = "ABC"
names = []
for i in range(1000):
    if len(names) == 100:
        break
    name = ""
    for j in range(4):
        name = name + random.choice(chars)
    if name not in names:
        names.append(name)
for name in names:
    f = open("img/" + name + ".png", "w")
    f.close()
