# generator
import random

with open("11.txt", "w") as f:
    n = 10
    m = 3
    for i in range(n):
        a = [random.randint(1, 100) for _ in range(m)]
        print(*a, sep = ",", file = f)
