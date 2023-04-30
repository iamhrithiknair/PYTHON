n=20
list1=[]
for i in range(n):
	list1.append(int(input("enter the elements:")))
t1=tuple(list1)
print(t1, "\n--this is the original tuple")
list2=[]
for i in range(n):
	if t1[i]%2==0:
		list2.append(t1[i])
	
t2=tuple(list2)
print(t2,"\n--this is the even tuple")

		
