# # 最后一题

class Person:
    def __init__(x, name, age, sex):
        x.name= name
        x.age= age
        x.sex= sex
    def personInfo(x):
        print("名字", x.name)
        print("年龄", x.age)
        print("性别", x.sex)
class Student(Person):
    def __init__(x, name, age, sex, college, classroom):
        super().__init__(name, age, sex)
        x.college= college
        x.classroom= classroom
    def personInfo(x):
        super().personInfo()
        print("学院", x.college)
        print("班级", x.classroom)
    def __str__(x):
        return f"名字{x.name}，年龄{x.age}，性别{x.sex}，学院{x.college}，班级{x.classroom}"
name= input("姓名：")
age= input("几岁：")
sex= input("男/女：")
college= input("学院：")
classroom= input("班级：")
Student(name, age, sex, college, classroom).personInfo()
print(Student(name, age, sex, college, classroom))

