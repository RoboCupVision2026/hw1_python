n=0
for i in range(1,5):
    a=i
    for j in range(1,5):
        if j != i:
            b=j
        else:
            continue
        for k in range(1,5):
            if k!=i and k!=j:
                c=k
                print(a*100+b*10+c)
                n+=1
            else:
                continue
print("总共能组成%d个三位数" % n)