

n=int(input("enter the size limit of list:"))
list1=[]
freq={}
for i in range(n):
	list1.append(input("enter the elements:"))

for item in list1:
	if item in freq:
		freq[item]+=1
		
	else:
		freq[item]=1
		
print("frequency of each element is :",freq)

