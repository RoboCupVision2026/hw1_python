num=(list(range(1,234)))
i=0
while len(num)>1:
    i=(i+2)%len(num)
    num.pop(i)
print(f"最后剩下的是{num[0]}号")