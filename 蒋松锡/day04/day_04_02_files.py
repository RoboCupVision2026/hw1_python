import os

os.mkdir("img")

for i in range(1,101):
    with open("img/" + str(i) + ".png", "w") as f:
        pass