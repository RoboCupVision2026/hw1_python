import random
import os

selected = random.sample(range(1, 101), 50)
for i in selected:
    os.rename("img/" + str(i) + ".png", "img/" + str(i) + ".jpg")
