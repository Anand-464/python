para = """ Python is an interpreted, high-level and general-purpose programming language. 
It is an object-oriented language too, which simply means it can model entities in the real world.
Python emphasizes the readability of code with its notable use of significant whitespace or indentation"""

print("Length is = ", len(para))

print("First chara = {}, Last chara = {}".format(para[0], para[-1]))

print("First 50 characters = ", para[:50])

print("Replacing python = ", para.replace("Python","PYTHON"))

print("To lowercase = ", para.lower())

print("Remove whitespace = ", para.strip())

print("Split the para = ", para.split())

if "course" in para:
    print("course is present")
else:
    print("course not present")
    
print("The course description is {} characters long and has {} words.".format(len(para), len(para.split())))