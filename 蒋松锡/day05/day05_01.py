import random
import statistics
with open("data.txt", "w") as f:
    for i in range(10):

        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)

        line = f"{a},{b},{c}\n"
        f.write(line)

with open("data.txt", "r") as f:
    numbers = []
    for line in f:
        parts = line.strip().split(",")
        number = int(parts[1])
        numbers.append(number)
    print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers) / len(numbers))
print(statistics.median(numbers))