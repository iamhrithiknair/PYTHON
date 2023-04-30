lb=int(input("enter lb:"))
ub=int(input("enter ub:"))
flag=True
for i in range(lb,ub+1):
	if i>1:
		flag=True
		for j in range(2,i):
			if i%j==0:
				flag=False
				break
				
		if flag:
			print(num)


				
