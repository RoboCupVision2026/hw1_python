sum=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            num=100*i+10*j+k
            if i!=j and i!=k and j!=k:
                print(num)
                sum+=1
print(f"一共有{sum}个数")
