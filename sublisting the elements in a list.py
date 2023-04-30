
n=int(input("enter the size limit of list:"))
list1=[]
for i in range(n):
	list1.append(input("enter the elements:"))
m=int(input("enter the lowerbound:"))
n=int(input("enter the upperbound:"))
s=list1[m:n]
print(s)
