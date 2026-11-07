count = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                sum = a*100 + b*10 +c
                print(sum)
                count+=1
print("总数等于：", count)