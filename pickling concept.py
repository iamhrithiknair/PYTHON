import pickle


info = {}
for i in range(4):
    rollno = int(input("Enter rollno: "))
    name = input("Enter name: ")
    
    info[rollno] = name

f1 = open("info.bin","wb+")
pickle.dump(info, f1)
print(info)
f1.close()

f2 = open("info.bin", "rb")
loaded_info = pickle.load(f2)
print("Loaded info:", loaded_info)
f2.close()

