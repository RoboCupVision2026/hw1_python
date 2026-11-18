import random

with open("numbers.txt", "w") as f:
    for i in range(10):
        f.write(f"{random.randint(1, 100)},{random.randint(1, 100)},{random.randint(1, 100)}\n")

a = []
with open("numbers.txt") as f:
    for s in f:
        a.append(int(s.split(",")[1]))

a.sort()
print(max(a))
print(min(a))
print(sum(a) / len(a))
print((a[4] + a[5]) / 2)
