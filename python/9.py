from pathlib import Path
import random
import string

if __name__ == "__main__":
    img_dir = Path("img")
    img_dir.mkdir(exist_ok=True)

    for i in range(100):
        name_chars = string.ascii_uppercase + string.digits
        file_stem = ''.join(random.choices(name_chars, k=4))
        file_path = img_dir / f"{file_stem}.png"
        file_path.touch()
