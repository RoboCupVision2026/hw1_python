class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"性别：{self.gender}")

class Student(Person):
    def __init__(self,name,age,gender,college,class_number):
        super().__init__(name,age,gender)
        self.college = college
        self.class_number = class_number

    def personinfo(self):
        super().personinfo()
        print(f"学院：{self.college}")
        print(f"班级：{self.class_number}")

    def __str__(self):
        return f"姓名：{self.name}\n年龄：{self.age}\n性别：{self.gender}\n学院：{self.college}\n班级：{self.class_number}"