from pathlib import Path
import random
import string

Path("img").mkdir(exist_ok=True)
used = set()
while len(used) < 100:
    name = "".join(random.choices(string.ascii_letters + string.digits, k=4)) + ".png"
    if name in used: continue
    used.add(name)
    (Path("img") / name).touch()
