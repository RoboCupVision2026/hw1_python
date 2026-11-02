int_list = list(range(1,234))
count = 0
idx = 0
while len(int_list) != 1:
    count = count + 1
    if count % 3 == 0:
        int_list.pop(idx)
    else:
        idx = idx + 1
    if idx>=len(int_list):
        idx = 0
print(int_list)