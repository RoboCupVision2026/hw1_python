class Person:
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
	def personInfo(self):
		print("姓名："+self.name)
		print("年龄："+str(self.age))
		print("性别："+self.gender)
class Student(Person):
	def __init__(self,name,age,gender,college,class_n):
		super().__init__(name,age,gender)
		self.college=college
		self.class_n=class_n
	def personInfo(self):
		super().personInfo()
		print("学院："+self.college)
		print("班级："+self.class_n)
	def __str__(self):
		return "学生信息"+self.name+""+str(self.age)+"岁"+self.college+""+self.class_n
