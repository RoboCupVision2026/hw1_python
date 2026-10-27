m=0
for i in range(4):
    for j in range(4):
        for k in range(4):
            n=(i+1)*100+(j+1)*10+k+1
            if (i!=j)and(j!=k)and(k!=i):
                print(n)
                m+=1
print("共有",m,"个三位数")