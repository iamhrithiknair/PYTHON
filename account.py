#creating objects

class Account:
	def __init__(self,name,account_no,account_type,balance):
		
		self.name=name
		self.account_no=account_no
		self.account_type=account_type
		self.balance=balance
		
	def deposit(self,amount):
		self.balance+=amount
		
	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance-=amount
			
		else:
			print("Insufficient funds")
			
	def readData(self):
		self.name=input("enter name:")
		self.account_no=input("enter account no:")
		self.account_type=input("enter type of the account:")
		
		
			
	def display(self):
		print("Name of the depositor:",self.name)
		print("Account No:",self.account_no)
		print("Account Type:",self.account_type)
		print("Balance:",self.balance)
		
customer=Account("","","",1000)
customer.readData()
customer.deposit(int(input("enter amount to deposit:")))


while(True):
	a=input("do you wish to withdraw:")
	if a=="yes":
		customer.withdraw(int(input("enter amount to withdraw:")))
		break
	else:
		break

customer.display()
	
	
