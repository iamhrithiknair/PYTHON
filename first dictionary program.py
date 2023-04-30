marks={}
n=int(input("enter the limit:"))
for i in range(n):
	student_name=input("enter student's name:")
	student_marks=int(input("enter student's marks:"))
	marks[student_name]=student_marks
print(marks)
