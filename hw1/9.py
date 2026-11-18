import os

os.makedirs("img", exist_ok=True)
for i in range(1, 101):
    open(f"img/{i}.png", "w").close()
