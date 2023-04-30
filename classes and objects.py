class Staff:
	def __init__(self,staff_code,staff_name):
		self.staff_code=staff_code
		self.staff_name=staff_name
		
class Teacher(Staff):
	def __init__(self,staff_code,staff_name,subject,publication):
		
		super().__init__(staff_code,staff_name)
		self.subject=subject
		self.publication=publication
		
	def readData(self):
		
		self.staff_code=input("enter staff code:")
		self.staff_name=input("enter staff name:")
		self.subject=input("enter subject:")
		self.publication=input("published(y/n):")
		
	def printData(self):
		
		print("Staff Code:",self.staff_code)
		print("Staff Name:",self.staff_name)
		print("Subject:",self.subject)
		print("Publication:",self.publication)
		
class Typist(Staff):
	def __init__(self,staff_code,staff_name,speed):
		
		super().__init__(staff_code,staff_name)
		self.speed=speed
		
	def readData(self):
		
		self.staff_code=input("enter staff code:")
		self.staff_name=input("enter staff name:")
		self.speed=input("enter typing speed in words per min:")
	
	def printData(self):
		
		print("Staff Code:",self.staff_code)
		print("Staff Name:",self.staff_name)
		print("Speed per min:",self.speed)
		
teacher=Teacher("","","","")
teacher.readData()
teacher.printData()

typist=Typist("","","")
typist.readData()
typist.printData()


