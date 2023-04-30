def dec(n):
	
	result=0
	for digit in n:
		result=result*2 + int(digit)
		
	return result
	
n=input("enter binary:")
print(dec(n))
