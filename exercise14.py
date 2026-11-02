import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path1="test.txt"
file_path2="copy_test.txt"
with open(file_path1, "r", encoding="utf-8") as f1, open(file_path2, "r", encoding="utf-8") as f2:
    content1=f1.readlines()
    content2=f2.readlines()
    arr_a=np.array(content1)
    arr_b=np.array(content2)
    com=(arr_a==arr_b)
    difrows=np.where(com==False)[0]
    print("不同的行号：", difrows+1)

