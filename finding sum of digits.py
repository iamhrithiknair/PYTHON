def sum(n):
	s=0
	while(n!=0):
		s=s+n%10
		n=n//10 #n//=10
	return s
	
a=int(input("enter number:"));
print("sum is:",sum(a))
