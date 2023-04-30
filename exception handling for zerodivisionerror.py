a=int(input("enter first no:"))
b=int(input("enter second no:"))

try:
	result=a/b
	print(result)
	
except ZeroDivisionError as e:
	print("can't divide by zero")
