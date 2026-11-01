count=0
for a in range(1,5):
    for b in range(1,5):
        if b==a:
            continue
        for c in range(1,5):
            if c==a or c==b:
                continue
            count+=1
            print(100*a+10*b+c)
print(f"共{count}个")