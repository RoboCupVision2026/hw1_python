nums = [1,2,3,4]
count = 0
results = []
for i in nums:
    for j in nums:
        for k in nums:
            if i != j != k:
                count +=1
                results.append(i*100+j*10+k)
print("个数：",count)
print("各是：",results)