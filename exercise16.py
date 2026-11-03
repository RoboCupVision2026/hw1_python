class Person:
    name="zhangsan"
    age=20
    gender="male"
    def personinfo(self):
        print("name:",Person.name)
        print("age:",Person.age)
        print("gender:",Person.gender)

class Student(Person):
    college="mechanical engineering"
    Class="2504"
    def studentinfo(self):
        Person().personinfo()
        print("college:",Student.college)
        print("class:",Student.Class)
    def __str__(self):
        context=Student().studentinfo()
        return context
Student().__str__()
    
