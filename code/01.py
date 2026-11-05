# # 第一次 Python 作业
# 姓名：郝子翔
# 
# ## 第一题：组成三位数

count=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
             if a !=b and a != c and b != c:
                 n= a*100+b*10+c
                 print(n)
                 count= count + 1
print("有", count ,"个")

