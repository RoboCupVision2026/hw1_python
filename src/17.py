class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.sex}")


class Student(Person):
    def __init__(self, name, age, sex, college, class_):
        super().__init__(name, age, sex)
        self.college = college
        self.class_ = class_

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.class_}")

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.sex}，学院：{self.college}，班级：{self.class_}"


student = Student("李昊轩", 19, "男", "强芯", "2501")
student.personInfo()
print(student)
