file1=input("enter a file name to open:")
f=open(file1,"r+")
file_contents=f.readline()

for line in file_contents.split():
	if line==line[::-1]:
		print(line)
f.close()
