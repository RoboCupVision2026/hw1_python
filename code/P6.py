class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print("姓名：",self.name)
        print("年龄：",self.age)
        print("性别：",self.sex)

class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        super().__init__(name,age,sex)
        self.college=college
        self.banji=banji
    def personInfo(self):
        super().personInfo()
        print("学院：",self.college)
        print("班级：",self.banji)
    def __str__(self):
        info="学生信息：姓名:"+self.name+"，年龄:"+str(self.age)+"，性别:"+self.sex+"，学院:"+self.college+"，班级:"+self.banji
        return info

if __name__=="__main__":
    stu=Student("李四",19,"女","人工智能学院","AI2班")
    stu.personInfo()
    print("-"*30)
    print(stu)