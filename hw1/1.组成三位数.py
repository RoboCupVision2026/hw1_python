nums=[1,2,3,4]
ans=0
anss=[]
for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1!=num2 and num1!=num3 and num2!=num3:
                ans+=1
                anss.append(num1*100+num2*10+num3)
print(ans)
for num in anss:
    print(num)