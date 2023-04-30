
n=int(input("enter the limit:"))
list1=[]
for i in range(n):
	list1.append(int(input("enter the elements:")))
t1=tuple(list1)
print(t1, "\n--this is the packing of the list")

s=0
for i in range(n):
	s=s+t1[i]
print(s,"is the sum")

