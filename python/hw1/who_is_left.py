list2=list(range(1,234))
while len(list2)>2:
    list2.pop(2)
    list3=[]
    for i in range(len(list2)):
        list3.append(list2[(i+2)%len(list2)])
    list2=list3.copy()
print(list2[1])