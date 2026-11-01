# 有233个人围成圈进行约瑟夫抽杀，问最后在几号的人活了下来？
people = [i for i in range(1, 234)]
cnt = 0
index = 0

while len(people) >1:
    cnt += 1
    if cnt == 3:
        people.pop(index)
        cnt = 0
        index = index % len(people)
    else:
        index = (index + 1) % len(people)
print(f"最后剩下的是{people[0]}号")