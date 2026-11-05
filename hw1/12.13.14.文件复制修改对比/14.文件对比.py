from pathlib import Path 
rootDir=Path(__file__).parent
with open(rootDir/"test.txt","r",encoding="utf-8") as fOri,\
    open(rootDir/"copy_test.txt","r",encoding="utf-8") as fCopy:
    lines1=fOri.readlines()
    lines2=fCopy.readlines()
    if len(lines1)==len(lines2):
        status=True
        for i in range(len(lines1)):
            if lines1[i] != lines2[i]:
                print("两份文件的第"+str(i+1)+"行不相同")
                status=False
        if status:
            print("两份文件完全相同！")
    else:
        print("两份文件行数不相等，无法对比！")