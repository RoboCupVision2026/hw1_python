# 第六题：找 bug
list=list(range(1000))
for idx in range(len(list)-1,-1,-1):
    print(idx)
    if list[idx]%2==1:
        list.pop(idx)
print(list)