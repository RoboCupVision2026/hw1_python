# 第七题：最后剩下谁
list = list(range(234))
list.remove(0)
count = 0
idx = 0
while len(list) > 1:
    if (count == 3):
        list.pop(idx)
        count = 0
    count += 1
    idx += 1
    if (idx >= len(list)):
        idx = 0
print(list[0])
