class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, college, class_name):
        super().__init__(name, age, gender)
        self.college = college
        self.class_name = class_name

    def personInfo(self):
        super().personInfo()
        print(f"学院: {self.college}, 班级: {self.class_name}")

    def __str__(self):
        return f"Student(姓名={self.name}, 年龄={self.age}, 性别={self.gender}, 学院={self.college}, 班级={self.class_name})"