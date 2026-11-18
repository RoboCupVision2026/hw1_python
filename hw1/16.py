class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(self.name, self.age, self.gender)


class Student(Person):
    def __init__(self, name, age, gender, college, clazz):
        super().__init__(name, age, gender)
        self.college = college
        self.clazz = clazz

    def personInfo(self):
        super().personInfo()
        print(self.college, self.clazz)

    def __str__(self):
        return f"{self.name} {self.age} {self.gender} {self.college} {self.clazz}"


s = Student("张三", 19, "男", "计算机学院", "计算机2501")
s.personInfo()
print(s)
