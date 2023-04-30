n=int(input("enter the limit:"))
list1=[]
for i in range(n):
	list1.append(input("enter the elements:"))
t1=tuple(list1)
print(t1, "\n--this is the tuple")
data=input("type the element to search:")
for i in range(n):
	if t1[i]==data:
		print(t1[i],"found")
		break
	else:
		print("not found")

