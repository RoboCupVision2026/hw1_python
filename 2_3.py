n=input("请输入任意位数的正整数：")
print("它是",len(n),"位数")
for i in n[::-1]:
    print(i,end="")