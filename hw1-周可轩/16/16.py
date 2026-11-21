"""
类的继承与魔术方法
题目：
1. 创建Person类，属性有姓名、年龄、性别，创建一个方法personInfo，打印这个人的信息。
2. 创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，除了调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来。
3. 重写__str__方法，返回student的信息。
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, college, class_):
        super().__init__(name, age, gender)
        self.college = college
        self.class_ = class_

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.class_}")

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，学院：{self.college}，班级：{self.class_}"