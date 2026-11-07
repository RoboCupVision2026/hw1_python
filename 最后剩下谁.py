people = list(range(1,234))
idx = 0
while len(people) > 1:
    idx = (idx + 2) % len(people)
    people.pop(idx)
print("最后剩下的人是：", people[0])