f1=open("test.txt","r")
list1=f1.readlines()
f1.close()

f2=open("copy_test.txt","r")
list2=f2.readlines()
f2.close()

maxline=len(list2)

for i in range(maxline):
    if list1[i]!=list2[i]:
        print("different line number:",i+1)

for i in range(len(list2),len(list1)):
    print("different line number:", i+1)
