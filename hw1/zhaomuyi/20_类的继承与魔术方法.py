# 第二十题：类的继承与魔术方法
# 题目：
#   1. 创建 Person 类，属性有姓名 name、年龄 age、性别 gender，
#      创建方法 personInfo，打印这个人的信息；
#   2. 创建 Student 类，继承 Person 类，属性有学院 college、班级 class，
#      重写方法 personInfo：除了调用父类方法打印个人信息外，
#      将学生的学院、班级信息也打印出来；
#   3. 重写 __str__ 魔术方法，返回 student 的信息。


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print("姓名：{}，年龄：{}，性别：{}".format(self.name, self.age, self.gender))


class Student(Person):
    def __init__(self, name, age, gender, college, clazz):
        super().__init__(name, age, gender)   # 调用父类构造
        self.college = college
        self.clazz = clazz

    def personInfo(self):
        super().personInfo()                  # 先打印父类信息
        print("学院：{}，班级：{}".format(self.college, self.clazz))

    def __str__(self):
        return "Student({}, {}, {}, {}, {})".format(
            self.name, self.age, self.gender, self.college, self.clazz)


if __name__ == "__main__":
    s = Student("赵牧怡", 19, "女", "机械工程学院", "钱元培班25")
    print("--- 调用 personInfo() ---")
    s.personInfo()
    print("--- 调用 __str__()（直接 print 对象）---")
    print(s)
