class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名: {self.name}，年龄: {self.age}，性别: {self.gender}")

    def __str__(self):
        return f"Person(姓名={self.name}, 年龄={self.age}, 性别={self.gender})"

    def __repr__(self):
        return self.__str__()


class Student(Person):
    def __init__(self, name, age, gender, college, class_name):
        super().__init__(name, age, gender)
        self.college = college
        self.class_name = class_name

    def personInfo(self):
        super().personInfo()
        print(f"学院: {self.college}，班级: {self.class_name}")

    def __str__(self):
        return (
            f"Student(姓名={self.name}, 年龄={self.age}, 性别={self.gender}, "
            f"学院={self.college}, 班级={self.class_name})"
        )


def main():
    person = Person("张三", 35, "男")
    student = Student("梁煜炜", 20, "男", "计算机学院", "计算机 2401 班")

    print("Person 对象的 personInfo():")
    person.personInfo()
    print()

    print("Student 对象重写后的 personInfo():")
    student.personInfo()
    print()

    print(f"print(person) 调用 __str__: {person}")
    print(f"print(student) 调用 __str__: {student}")
    print(f"Student 是 Person 的子类: {isinstance(student, Person)}")
    print(f"方法解析顺序 MRO: {[cls.__name__ for cls in Student.__mro__]}")


if __name__ == "__main__":
    main()
