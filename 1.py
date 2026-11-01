count=0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and a != c:
                num=a * 100 + b * 10 + c
                print(num)
                count+=1
print("能組成的不同三位數有", count, "個")