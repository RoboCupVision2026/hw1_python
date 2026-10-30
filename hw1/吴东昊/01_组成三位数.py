a=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                a.append(i*100+j*10+k)
print(*a)
print("个数：",len(a))
