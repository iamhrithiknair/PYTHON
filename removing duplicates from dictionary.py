cars={}
n=int(input("enter the limit:"))
for i in range(n):
	brand=input("enter brand:")
	model=input("enter model:")
	cars[brand]=model
print(cars, "--this is the dictionary")


# Remove duplicate values in dictionary

temp={}
for k, v in cars.items():
	if v not in temp.values():
		temp[k]=v
print(temp)
