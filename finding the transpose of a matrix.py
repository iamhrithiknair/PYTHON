m=int(input("enter row of  matrix:"))
n=int(input("enter column of  matrix:"))

mat=[]
for i in range(m):
	row=[]
	for j in range(n):
		row.append(int(input("enter elements:")))
		
	mat.append(row)
	
print("matrix is:")
for i in range(m):
	for j in range(n):
		print(mat[i][j]," ",end=" ")
	print()
	
print("transpose is:\n")
for i in range(m):
	for j in range(n):
		print(mat[j][i]," ",end=" ")
	print()
