with open("test.txt","r") as f1,open("copy_test.txt","r") as f2:
    lines1=f1.readlines()
    lines2=f2.readlines()
if len(lines1)==len(lines2):
    for i in range(len(lines1)):
        if lines1[i]!=lines2[i]:
            print(i+1)
if len(lines1)>len(lines2):
        for i in range(len(lines2)):
            if lines1[i]!=lines2[i]:
                print(i+1)
        for j in range(len(lines2),len(lines1)):
            print(j+1)
if len(lines1)<len(lines2):
        for i in range(len(lines1)):
            if lines1[i]!=lines2[i]:
                print(i+1)
        for j in range(len(lines1),len(lines2)):
            print(j+1)