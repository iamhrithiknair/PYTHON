

cars={}
n=int(input("enter the limit:"))
for i in range(n):
	brand=input("enter brand:")
	model=input("enter model:")
	cars[brand]=model

print(cars,"\n --this is the original dictionary")

s=sorted(cars.items())
d=dict(s)
print(d)

sort={k:v for k, v in sorted(cars.items())}

print(sort)
