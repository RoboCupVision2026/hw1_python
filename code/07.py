# ## 第七题
# 

people= list(range(1, 234))
idx= 0
while len(people) > 1:
    idx= idx + 2
    idx= idx % len(people)  #"依次向前删除，加上除余考虑最后一位循环报数到第一位的情况"
    people.pop(idx)
print("最后剩下的是原来的", people[0], "号")

