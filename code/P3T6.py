#list为python自带关键字，最好不要用来做变量名
#循环遍历的同时删除了元素，导致一些元素被跳过，同时idx会跑到已经不存在的下标
num=list(range(1000))
new=[]
for x in num:
    if x%2==0: 
        new.append(x)
num=new
print(num)