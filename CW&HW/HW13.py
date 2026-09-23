num = int(input("Enter the no of students: ="))

f = open("students.txt","r")
print("\nExisting names")
for x in f:
    print(x.strip())
f.close()
    
f = open("students.txt", "a")
for i in range(num):
    names = input("\nenter names:= ")
    f.write(names + "\n")
f.close()

f = open("students.txt", "r")
print("\nupdated list")
for x in f:
    print(x.strip())
f.close()