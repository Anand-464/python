python_ = {"abhi", "john", "jane", "akash"}
data_science = {"alice", "bob", "asha", "akash"}

python_.add("peter")
print("added student = ",python_)

print("removing student = ",data_science.pop())

print("common student = ",python_.intersection(data_science))

print("in python not in data science = ",python_ - data_science)

print("combined list = ", python_.union(data_science))

courses = {
    "Python": len(python_),
    "Data science": len(data_science)
}
print("courses = ",courses)

for x in courses:
    print("Course:", x, ",", "Students:", courses[x])
    
new_dict = {x: courses[x]*2 for x in courses}
print("new dictionary = ", new_dict)