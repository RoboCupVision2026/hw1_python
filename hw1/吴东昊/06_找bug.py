# 删除后下标错位、越界；避免覆盖list
a=list(range(1000))
for i in range(len(a)-1,-1,-1):
    if a[i]%2==1:
        a.pop(i)
print(a)
