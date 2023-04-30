
n=int(input("enter the limit:"))
list1=[]
for i in range(n):
	list1.append(input("enter the elements:"))
t1=tuple(list1)
print(t1, "\n--this is the packing of the tuple")

print("on unpacking:")

for i in range(n):
	print(t1[i])

