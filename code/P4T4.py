import random
import string
from pathlib import Path

image=Path("random image")
image.mkdir(exist_ok=True)
chars=string.ascii_uppercase+string.digits
for i in range(100):
    name=''.join(random.choice(chars) for j in range(4))
    file=image/f"{name}.png" 
    file.touch()