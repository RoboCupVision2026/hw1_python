class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.gender)


class Student(Person):
    def __init__(self, name, age, gender, college, class_):
        super().__init__(name, age, gender)
        self.college = college
        self.class_ = class_

    def personInfo(self):
        super().personInfo()
        print("学院：", self.college)
        print("班级：", self.class_)

    def __str__(self):
        return (f"姓名：{self.name}，年龄：{self.age}，"
                f"性别：{self.gender}，学院：{self.college}，"
                f"班级：{self.class_}")


student = Student("张三", 19, "男", "计算机学院", "计算机1班")

student.personInfo()

print(student)