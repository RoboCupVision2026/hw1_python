def fb(a):
    if (a==1):
        return 0
    elif (a==2):
        return 1
    else:
        return fb(a-1)+fb(a-2)

for i in range(19):
    print(fb(i+1),end="、")
print(fb(20),end="")