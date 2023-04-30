

n=int(input("enter the limit:"))
list1=[]
for i in range(n):
	list1.append(input("enter the elements:"))
t1=tuple(list1)
print(t1, "\n--this is the packing of the list")

s=sorted(list1)
list2=[]
for i in range(n):
	list2.append(s[i])

t2=tuple(list2)
print(t2)


