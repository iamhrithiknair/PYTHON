m1=int(input("enter row of first matrix:"))
n1=int(input("enter column of first matrix:"))

m2=int(input("enter row of second matrix:"))
n2=int(input("enter column of third matrix:"))

if m1==n2 or n1==m1:
	mat1=[]
	mat2=[]
	mat3=[]

else:
	print("can't multiply")
	exit()
	
for i in range(m1):
	row=[]
	for j in range(n1):
		row.append(int(input("enter elements to the first matrix:")))
	
	mat1.append(row)
	
for i in range(m2):
	row=[]
	for j in range(n2):
		row.append(int(input("enter elements to the second matrix:")))
		
	mat2.append(row)
	

for i in range(m1):
	row=[]
	for j in range(n2):
		c=0
		for k in range(n1):
			c=c+(mat1[i][k]*mat2[k][j])
			row.append(c)
			
	mat3.append(row)
	

print("on multiplication:\n")

for i in range(m1):
	for j in range(n2):
		print(mat3[i][j]," ",end=" ")
	print()
