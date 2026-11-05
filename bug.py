list=list(range(1000))
i=0
while i<500:
    if list[i]%2==1:
        list.pop(i)
        continue
    else:
        print(list[i])
        i+=1
        continue
