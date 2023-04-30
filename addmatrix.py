m1=int(input("enter row of first matrix:"))
n1=int(input("enter column of first matrix:"))

m2=int(input("enter row of second matrix:"))
n2=int(input("enter column of second matrix:"))

if m1==n2 or n1==m2:
	mat1=[]
	mat2=[]
	mat3=[]
	
else:
	print("can't add")
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
		row.append(mat1[i][j]+mat2[i][j])
		
	mat3.append(row)
	
for i in range(m1):
	for j in range(n1):
		print(mat3[i][j]," ",end=" ")
		
	print()
