import os
import random
from pathlib import Path
import string

# #1.组成三位数
# a_1 = [1,2,3,4]
# count = 0
# for i in a_1:
#     for j in a_1:
#         for k in a_1:
#             if(i!=j and i!=k and j!=k):
#                 #print(i*100+j*10+k)
#                 count = count + 1
#print(count)

# #2.排序
# a_2 = []
# for i in range(0,3,1):
#     x = int(input())
#     a_2.append(x)
# a_2.sort()
#print(a_2)

# #3.斐波那契数列
# num1 = 0
# num2 = 1
# a_3 = [0,1]
# for i in range(18):
#     a_3.append(a_3[i] + a_3[i+1])
# print(a_3)

# #4.数字位数
# num_4 = int(input())
# num_list_4 = []
# count = 0
# while(num_4>=10):
#     x = num_4 %10
#     num_4 = num_4//10
#     num_list_4.append(x)
#     count = count + 1
# num_list_4.append(num_4)
# print(num_list_4)
# print(count+1)

# #5.回文数
# num_5 = int(input())
# num_list_5 = []
# count = 0
# result = 1
# while(num_5>=10):
#     x = num_5 %10
#     num_5 = num_5//10
#     num_list_5.append(x)
#     count = count + 1
# num_list_5.append(num_5)
# count = count + 1
# for i in range(0,count//2,1):
#     if(num_list_5[i] != num_list_5[-(i+1)]):
#         result = 0
#         break
# if(result == 0):
#     print("false")
# else:
#     print("true")      

# #6.找bug
# #因为python的list可变，所以每删除一个数，下标都会偏移，而且后续还会越界

# #7.最后还剩谁
# list_7 = list(range(1, 234))
# idx_7 = 0
# while len(list_7) > 1:
#     idx_7 = (idx_7 + 2) % len(list_7) 
#     list_7.pop(idx_7)
    
# print("最后留下的是原来第", list_7[0], "号")

# #8.随机数文件
# with open("data.txt", "w") as f_8:
#     for i_4_3 in range(100000):
#         # 生成 1~100 的随机整数，转为字符串后写入，并加上换行符
#         num_4_3 = random.randint(1, 100)
#         f_8.write(str(num_4_3) + "\n")

# print("data.txt 创建完成")

# #9.创建顺序文件
# dir_9 = Path("img")
# dir_9.mkdir(parents=True,exist_ok=True)
# chars_9 = string.ascii_uppercase + string.digits

# for i_9 in range(100):
#     random_str_9 = "".join(random.choices(chars_9,k=4))
#     file_name_9 = random_str_9 + ".png"
#     file_path_9 = dir_9 / file_name_9
#     file_path_9.touch()

# #10.文件改名
# dir_10 = Path("img")
# file_list_10 = list(dir_10.iterdir())
# random.shuffle(file_list_10)
# chars_10 = string.ascii_lowercase + string.digits
# for i_10 in range(50):
#     old_file_10 = file_list_10[i_10]
#     while True:
#         new_name_10 = "".join(random.choices(chars_10,k=4)) + ".jpg"
#         new_file_10 = dir_10 / new_name_10
#         if not new_file_10.exists():
#             break
#     old_file_10.rename(new_file_10)
# print("已将50个文件改名为.jpg结尾")

# #11.文件输入
# with open("num.txt", "w") as f_11:
#     for i in range(10):
#         row_11 = [random.randint(1, 100) for k in range(3)]
#         f_11.write(str(row_11[0]) + "," + str(row_11[1]) + "," + str(row_11[2]) + "\n")
# arr_11 = []
# with open("num.txt", "r") as f_11:
#     for line in f_11:
#         x_11 = line.strip().split(",")
#         arr_11.append(int(x_11[1]))
# arr_11.sort()
# n_11 = len(arr_11)
# print("最大值:", arr_11[-1])
# print("最小值:", arr_11[0])
# print("平均值:", sum(arr_11) / n_11)
# if(n_11 % 2 == 1):
#     mid_11 = arr_11[n_11 // 2]
# else:
#     mid_11 = (arr_11[n_11 // 2 - 1] + arr_11[n_11 // 2]) / 2
# print("中位数:", mid_11)

# #12.文件复制
# i_12 = int(input())
# chars_12 = string.ascii_letters + string.digits + string.punctuation + " "
# with open("test.txt", "w") as f_12:
#     for k in range(i_12):
#         line_12 = "".join(random.choices(chars_12,k=random.randint(5, 20)))
#         f_12.write(line_12 + "\n")
# with open("test.txt", "r") as f_12, open("copy_test.txt", "w") as g_12:
#     for line in f_12:
#         g_12.write(line)
# print("test.txt 和 copy_test.txt 创建完成")

# #13.文件修改
# with open("test.txt", "r+") as f_13:
#     content_13 = f_13.read()
#     f_13.seek(0)
#     f_13.write("python" + content_13 + "python")
# print("已在test.txt开头和结尾追加python")

# #14.文件对比
# with open("test.txt", "r") as f_14, open("copy_test.txt", "r") as g_14:
#     list_14 = f_14.readlines()
#     list2_14 = g_14.readlines()
# n_14 = max(len(list_14), len(list2_14))
# for i_14 in range(n_14):
#     if(i_14 >= len(list_14) or i_14 >= len(list2_14) or list_14[i_14] != list2_14[i_14]):
#         print("第", i_14 + 1, "行不同")

# #15.文件批量创建
# i_15 = int(input())
# j_15 = int(input())
# dir_15 = Path("test")
# dir_15.mkdir(exist_ok=True)
# chars_15 = string.ascii_letters + string.digits
# for k in range(i_15):
#     while True:
#         file_name_15 = "".join(random.choices(chars_15,k=4)) + ".txt"
#         file_15 = dir_15 / file_name_15
#         if not file_15.exists():
#             break
#     with open(file_15, "w") as f_15:
#         for m in range(j_15):
#             line_15 = "".join(random.choices(chars_15,k=random.randint(5, 20)))
#             f_15.write(line_15 + "\n")
# for file_15 in list(dir_15.iterdir()):
#     with open(file_15, "r") as f_15:
#         lines_15 = f_15.readlines()
#     with open(file_15, "w") as f_15:
#         for line_15 in lines_15:
#             f_15.write(line_15.rstrip("\n") + "-python\n")
#     file_15.rename(dir_15 / (file_15.name + "-python"))
# print("test目录下的文件已批量处理完成")

# #16.类的继承与魔术方法
# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def personInfo(self):
#         print("姓名:", self.name, "年龄:", self.age, "性别:", self.sex)
#
# class Student(Person):
#     def __init__(self, name, age, sex, college, class_):
#         super().__init__(name, age, sex)
#         self.college = college
#         self.class_ = class_
#     def personInfo(self):
#         super().personInfo()
#         print("学院:", self.college, "班级:", self.class_)
#     def __str__(self):
#         return "姓名:" + self.name + " 年龄:" + str(self.age) + " 性别:" + self.sex + " 学院:" + self.college + " 班级:" + self.class_
#
# a_16 = Student("张三", 20, "男", "计算机学院", "1班")
# a_16.personInfo()
# print(a_16)

