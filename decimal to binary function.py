def bin(n):
	
	if n>1:
		bin(n//2)
	print(n%2,end=' ')
n=int(input("enter no:"))
print(bin(n))
