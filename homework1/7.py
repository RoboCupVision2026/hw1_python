people = []
for i in range(1, 234):
    people.append(i)
idx = 0
for k in range(232):
    for step in range(2):
        idx = idx + 1
        if idx == len(people):
            idx = 0
    people.pop(idx)
    if idx == len(people):
        idx = 0
print("最后剩下的是", people[0], "号")