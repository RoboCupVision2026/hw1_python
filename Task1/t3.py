def feb(n):
    if n==1:return 0
    elif n==2:return 1
    else:return feb(n-2)+feb(n-1)
for i in range(1,21):
    if i!=20:print(feb(i),end=",")
    else:print(feb(i))
