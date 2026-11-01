class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, college, cls):
        super().__init__(name, age, gender)
        self.college = college
        self.cls = cls

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.cls}")

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，学院：{self.college}，班级：{self.cls}"

if __name__ == "__main__":
    s = Student("小明", 19, "男", "计算机学院", "计科2501")
    s.personInfo()
    print(s)
