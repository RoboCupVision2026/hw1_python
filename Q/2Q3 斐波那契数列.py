a=[0 for _ in range(20)]
a[1]=1
for i in range(18):
    a[i+2]=a[i+1]+a[i]
print(*a)