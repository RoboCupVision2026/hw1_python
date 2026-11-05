num=input("请输入一个正整数：")
length=len(num)
status=True
for i in range(length//2):
    if num[i]!=num[length-i-1]:
        status=False
        break
if status:
    print(f"{num}是回文数！")
else:
    print(f"{num}不是回文数！")