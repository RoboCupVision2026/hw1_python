import random
with open('data.txt', 'w',encoding='utf-8') as f:
    for i in range(1,100001):
        if i<=100000-1:
            f.write(str(random.randint(1,100))+'\n')
        else:
            f.write(str(random.randint(1,100)))
print("文件data.txt创建完成")