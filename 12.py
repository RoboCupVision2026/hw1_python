import random
def random_ascii_str():
    s = ""
    length = random.randint(5,15)
    for _ in range(length):
        char_code = random.randint(32,126)
        s += chr(char_code)
    return s
i = int(input("請輸入要生成的行數 i："))
with open("test.txt", "w", encoding="ascii") as f:
    for _ in range(i):
        line = random_ascii_str()
        f.write(line + "\n")
with open("test.txt", "r", encoding="ascii") as src, open("copy_test.txt", "w", encoding="ascii") as dst:
    dst.write(src.read())

print("test.txt 和 copy_test.txt 建立完成")