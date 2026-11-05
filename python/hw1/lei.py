class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"{self.name} {self.age} {self.gender}")

    def __str__(self):
        return f"{self.name}"

class Student(Person):
    def __init__(self, name, age, gender, college, klass):
        super().__init__(name, age, gender)
        self.college = college
        self.klass = klass

    def personInfo(self):
        super().personInfo()
        print(self.college, self.klass)