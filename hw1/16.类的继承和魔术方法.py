class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=int(age) 
        self.gender=gender 

    def personInfo(self):
        print(f"该人类的姓名为{self.name}，年龄为{self.age}，性别为{self.gender}")

class Student(Person):
    def __init__(self,name,age,gender,college,schoolClass):
        super().__init__(name,age,gender)
        self.college=college
        self.schoolClass=schoolClass

    def personInfo(self):
        print(f"该学生的姓名为{self.name}，年龄为{self.age}，性别为{self.gender}，学院为{self.college}，班级为{self.schoolClass}")

    def __str__(self):
        return f"一名学生，姓名为{self.name}，年龄为{self.age}，性别为{self.gender}，学院为{self.college}，班级为{self.schoolClass}"