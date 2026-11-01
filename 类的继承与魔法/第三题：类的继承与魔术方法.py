# 创建Person类，属性有姓名、年龄、性别，创建方法personInfo，打印这个人的信息
class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.sex}")

# 创建Student类，继承Person类，属性有学院college，班级class，重写方法personInfo打印学院和班级信息
class Student(Person):
    def __init__(self, name, age, sex, college, className):
        super().__init__(name, age, sex)
        self.college = college
        self.className = className

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.className}")

    #重写__str__方法，返回student信息
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.sex}，学院：{self.college}，班级：{self.className}"
