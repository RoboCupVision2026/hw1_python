import random
import statistics

with open ("data1.txt", "w+") as file:
    for i in range(10):
        for j in range(3):
            row = [str(random.randint(1, 100)) for j in range(3)]
            file.write(",".join(row) + "\n")
        
column = []
with open("data1.txt", "r") as file:
    for line in file:
        column.append(int(line.strip().split(",")[1]))
        
print("max: ", max(column))
print("min: ", min(column))
print("average: ", statistics.mean(column))
print("median: ", statistics.median(column))