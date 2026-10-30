import random
import string
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent / "img"
    directory.mkdir(exist_ok=True)
    alphabet = string.ascii_uppercase + string.digits
    created = 0
    while created < 100:
        name = "".join(random.choices(alphabet, k=4)) + ".png"
        path = directory / name
        if not path.exists():
            path.touch(exist_ok=False)
            created += 1


if __name__ == "__main__":
    main()
