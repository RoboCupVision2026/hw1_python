class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def personInfo(self):
        print("name:",self.name)
        print("age:",self.age)
class Student(Person):
    def __init__(self,name,age,sex,college,class_num):
        super().__init__(name,age,sex)
        self.college = college
        self.class_num = class_num
    def personInfo(self):
        super().personInfo()
        print("college:",self.college)
        print("class_num:",self.class_num)
    def  __str__(self):
        return f"name:{self.name},age:{self.age},sex:{self.sex}college:{self.college},class_num:{self.class_num}"