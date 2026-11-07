
class Person:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def personInfo(self):
        print(f'姓名：{self.name}，年龄：{self.age}，性别：{self.gender}')
    
class Student(Person):
    def __init__(self,name,age,gender,college,clas):
        super().__init__(name,age,gender)
        self.college=college
        self.clas=clas
    
    def personInfo(self):
        super().personInfo()
        print(f'学院：{self.college}，班级：{self.clas}')
    
    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，学院：{self.college}，班级：{self.clas}'
    
p=Student('一一',190,'沃尔玛购物袋','奶龙学院','唱跳2502.5')
p.personInfo()
print(p)