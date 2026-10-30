import random
if __name__ == "__main__":
    with open("data.txt", "w", encoding="utf-8") as f:
        for _ in range(10000):
            num = random.randint(1, 100)
            f.write(f"{num}\n")
    print("生成完成")