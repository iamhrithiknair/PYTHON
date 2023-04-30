marks={}
n=int(input("enter the limit:"))
for i in range(n):
	student_name=input("enter student's name:")
	student_marks=int(input("enter student's marks:"))
	marks[student_name.title()]=student_marks
print(marks, "--this is the dictionary")

data=input("enter to search:")
for key in marks.items():
	if data in marks:
		print("found")
		break
	else:
		print("not found")
