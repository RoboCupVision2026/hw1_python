lst=list(range(1,234))
i=0
while len(lst)>1:
    i=(i+2)%len(lst)
    lst.pop(i)
print('留下的是原来的第',lst[0],'号','原索引为',lst[0]-1)