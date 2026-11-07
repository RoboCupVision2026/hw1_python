p=list(range(1,234))
num=233
cnum=1
while num>1:
    cnt=0
    while cnt<num:
        if cnum==3:
            p.pop(cnt)
            num-=1
            cnum=1
        else:
            cnt+=1
            cnum+=1
print(p[0])