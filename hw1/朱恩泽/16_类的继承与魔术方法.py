class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, college, class_name):
        super().__init__(name, age, gender)
        self.college = college
        self.class_name = class_name

    def personInfo(self):
        super().personInfo()
        print(f"学院：{self.college}，班级：{self.class_name}")

    def __str__(self):
        return (
            f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，"
            f"学院：{self.college}，班级：{self.class_name}"
        )


def main():
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    gender = input("请输入性别：")
    college = input("请输入学院：")
    class_name = input("请输入班级：")
    student = Student(name, age, gender, college, class_name)
    student.personInfo()
    print(student)


if __name__ == "__main__":
    main()
