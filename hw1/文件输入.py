file=open("1.txt",mode="wt")
from random import randint
for n in range(10):
	n1=randint(1,100)
	n2=randint(1,100)
	n3=randint(1,100)
	list=f"{n1},{n2},{n3}\n"
	file.write(list)
file.close()
import csv
import statistics
with open("1.txt",mode="rt") as f:
	cr=csv.reader(f)
	data=[]
	for line in cr:
		data.append(int(line[1]))
	print(data)
	t1=max_val=max(data)
	t2=min_val=min(data)
	t3=ave_val=statistics.mean(data)
	t4=mid_val=statistics.median(data)
	print(f"最大值:{t1},最小值:{t2},平均值:{t3},中位数:{t4}")
