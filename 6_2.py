#约瑟夫环
people = list(range(1, 234))
index = 0

while len(people) > 1:
    index = (index + 2) % len(people)
    people.pop(index)

print("最后剩下的是原来的第", people[0], "号。")
