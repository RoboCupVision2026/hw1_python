my_list = list(range(1,234))
idx = 0
while True:
    idx = (idx + 2) % len(my_list)
    my_list.pop(idx)
    if len(my_list) == 1:
        break
print(my_list[0])