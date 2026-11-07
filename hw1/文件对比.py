f1=open("test.txt",mode="rt")
list1=f1.readlines()
f1.close
f2=open("copy_test.txt",mode="rt")
list2=f2.readlines()
f2.close
for i in range(len(list1)):
	if list1[i]!=list2[i]:
		print(i+1)
