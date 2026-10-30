class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名:{self.name}, 年龄:{self.age}, 性别:{self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, college, cls):
        super().__init__(name, age, gender)
        self.college = college      
        self.cls = cls              
    def personInfo(self):
        super().personInfo()
        print(f"学院:{self.college}, 班级:{self.cls}")
    def __str__(self):
        return (f"Student(姓名={self.name}, 年龄={self.age}, "
                f"性别={self.gender}, 学院={self.college}, 班级={self.cls})")
p = Person("张三", 40, "男")
p.personInfo()
s = Student("李四", 20, "女", "计算机学院", "软件2001")
s.personInfo()        
print(s)               