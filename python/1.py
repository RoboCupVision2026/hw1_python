l = []

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                l.append(a*100+b*10+c)

print(f"能组成{len(l)}个")
print(l)