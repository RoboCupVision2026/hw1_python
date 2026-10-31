class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print(f"姓名: {self.name}, 年齡: {self.age}, 性別: {self.gender}")  

class student(person):
    def __init__(self, name, age, gender, college, cls):
        super().__init__(name, age, gender)
        self.college = college
        self.cls = cls

    def personinfo(self):
        super().personinfo()
        print(f"學院: {self.college}, 班級: {self.cls}")

    def __str__(self):
        return f"姓名: {self.name}, 年齡: {self.age}, 性別: {self.gender}, 學院: {self.college}, 班級: {self.cls}"
if __name__ == "__main__":
    s = student("張三", 19, "男", "電信學部", "信息工程2501班")
    s.personinfo()
    print(s)