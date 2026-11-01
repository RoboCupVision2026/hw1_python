err=[]
with open("test.txt","r") as f1,open("copy_test.txt","r") as f2:
    lines1=f1.readlines()
    lines2=f2.readlines()
    for i in range(1,min(len(lines1),len(lines2))+1):
        if(lines1[i-1]!=lines2[i-1]):
            err.append(i)
    for i in range(min(len(lines1),len(lines2))+1,max(len(lines1),len(lines2))+1):
        err.append(i)
if err:
    print(f"不一样的行有：第{'、'.join(map(str,err))}行（按更长的文件的行号算）")
else:
    print("每一行都相同")