import random
import string
from pathlib import Path

img_dir = Path("img")
img_dir.mkdir(exist_ok=True)

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
file_names = set()

while len(file_names) < 100:
    name = ''.join(random.choices(chars, k=4))
    file_names.add(name)

for name in file_names:
    file_path = img_dir / f"{name}.png"
    file_path.touch()