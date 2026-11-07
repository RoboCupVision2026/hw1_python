class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def personInfo(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}")
class Student(Person):
    def __init__(self, name, age, gender, college, classname):
        super().__init__(name, age, gender) 
        self.college = college
        self.classname = classname  
    def personInfo(self):
        super().personInfo() 
        print(f"学院: {self.college}, 班级: {self.classname}")
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 学院: {self.college}, 班级: {self.classname}"
if __name__ == "__main__":
    stu = Student("张三", 20, "男", "软件学院", "软件2601班")
    stu.personInfo() 
    print(stu)
