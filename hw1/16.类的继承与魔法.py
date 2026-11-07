class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(f"name:{self.name}    age:{self.age}    gender:{self.gender}")
class Student(Person):
    def __init__(self,name,age,gender,college,_class):
        super().__init__(name,age,gender)
        self.college=college
        self._class=_class
    def personInfo(self):
        super().personInfo()
        print(f"    college:{self.college}    class:{self._class}")
    def __str__(self):
        return f"name:{self.name}    age:{self.age}    gender:{self.gender}    college:{self.college}    class:{self._class}"