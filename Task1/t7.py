p=list(range(1,234))
i=0
count=1
while len(p)!=1:
    if count!=3:
        i=(i+1)%len(p)
        count+=1
    else:
        p.pop(i)
        i=i%len(p)
        count=1
print(f"最后留下的是原来第{p[0]}号的那一位")
