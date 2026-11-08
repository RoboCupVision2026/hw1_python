class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def personInfo(self):
        print(self.name)
        print(self.age)
        print(self.gender)

    def __str__(self):
        return f"{self.name}\n {self.age}\n {self.gender}"
class Student(Person):
    def __init__(self,name,age,gender,college,stu_class):
        super().__init__(name,age,gender)
        self.college=college
        self.stu_class=stu_class
    def personInfo(self):
        super().personInfo()
        print(self.college)
        print(self.stu_class)
    def __str__(self):
        return f"{self.name}\n {self.age}\n {self.college}\n {self.stu_class}"


