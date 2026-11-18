import os
import random

a = [f for f in os.listdir("img") if f.endswith(".png")]
for f in random.sample(a, 50):
    os.rename("img/" + f, "img/" + f[:-4] + ".jpg")
