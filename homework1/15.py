class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def personInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.sex)
class Student(Person):
    def __init__(self, name, age, sex, college, klass):
        Person.__init__(self, name, age, sex)
        self.college = college
        self.klass = klass
    def personInfo(self):
        Person.personInfo(self)
        print("学院：", self.college)
        print("班级：", self.klass)
    def __str__(self):
        return ("姓名：" + self.name + "，年龄：" + str(self.age) +
                "，性别：" + self.sex + "，学院：" + self.college +
                "，班级：" + self.klass)
p = Person("张三", 20, "男")
print("Person 的信息：")
p.personInfo()
s = Student("李四", 19, "女", "计算机学院", "软件1班")
print("Student 的信息：")
s.personInfo()
print("__str__ 打印：")
print(s)