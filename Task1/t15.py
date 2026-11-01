class Person:
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.gender=c
    def personinfo(self):
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"性别：{self.gender}")
class Student(Person):
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c)
        self.college=d
        self.classname=e
    def personinfo(self):
        super().personinfo()
        print(f"学院：{self.college}")
        print(f"班级：{self.classname}")
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，学院：{self.college}，班级：{self.classname}"