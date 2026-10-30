import random


def main():
    with open("data.txt", "w", encoding="utf-8") as file:
        for _ in range(10000):
            file.write(f"{random.randint(1, 100)}\n")


if __name__ == "__main__":
    main()
