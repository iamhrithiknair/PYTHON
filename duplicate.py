

n=int(input("enter the limit:"))
list1=[]
for i in range(n):
	list1.append(input("enter the elements:"))
t1=tuple(list1)
print(t1, "\n--this is the packing of the list")

print("duplicate elements are:")

for i in range(n):
	k=i+1
	for j in range(k,n):
		if t1[i]==t1[j]:
			print(t1[i])
