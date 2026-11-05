from pathlib import Path
import random
import string

Path("test").mkdir(exist_ok=True)
i=int(input())
j=int(input())

ascii_chars = string.ascii_letters + string.digits + string.punctuation

for k in range(i):
    with open(Path("test") / f"file{k}.txt", "w", encoding="utf-8") as f:
        for l in range(j):
            n = random.randint(1, 100)
            line = "".join(random.choice(ascii_chars) for m in range(n))
            f.write(line + "\n")

folder = Path("test")
files = sorted(folder.iterdir())

for p in files:

    with open(p, encoding="utf-8") as f:
        lines = f.readlines()

    with open(p, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "-python\n")

    new_name = p.stem + "-python" + p.suffix
    p.rename(p.with_name(new_name))