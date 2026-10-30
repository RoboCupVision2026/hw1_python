class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print(self.name,self.age,self.sex)
class Student(Person):
    def __init__(self,name,age,sex,college,cls):
        super().__init__(name,age,sex)
        self.college=college
        self.cls=cls
    def personInfo(self):
        super().personInfo()
        print(self.college,self.cls)
    def __str__(self):
        return f"{self.name} {self.age} {self.sex} {self.college} {self.cls}"
if __name__=="__main__":
    s=Student("张三",20,"男","计算机学院","1班")
    s.personInfo()
    print(s)
