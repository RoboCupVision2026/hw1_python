count=0
for a in range(1,5):
    for b in range(1,5):
        if b==a:
            continue
        for c in range(1,5):
            if c==a or c==b:
                continue
            print(100*a+10*b+c)
            count+=1
print("共",count,"个")