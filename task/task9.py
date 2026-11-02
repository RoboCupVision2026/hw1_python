#文件输入
from random import randint
with open("random_data.txt","w",encoding="utf-8") as f:
    for i in range(10):
        f.write(str(randint(1,100))+','+str(randint(1,100))+','+str(randint(1,100))+'\n')
list_2 = []
with open("random_data.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        new_line = line.split(',')
        list_2.append(int(new_line[1]))
from statistics import median
print("第二列的中位数是"+str(median(list_2)))
print("第二列的最大值是"+str(max(list_2)))
print("第二列的最小值是"+str(min(list_2)))
print("第二列的平均数是"+str(sum(list_2)/len(list_2)))
