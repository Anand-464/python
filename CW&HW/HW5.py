frontend = {"abhi", "john", "jane", "akash"}
backend = {"alice", "bob", "asha", "akash"}

backend.add("hari")
print("added student = ", backend)

print("removed student = ", frontend.pop())

print("in both = ", frontend & backend)

print("only in backend = ", backend - frontend)

print("total no. of unique stu = ", len(frontend | backend))

dict_ = {
    "Frontend":len(frontend),
    "Backend": len(backend)
}
print("dictionary = ", dict_)

for x in dict_:
    print("Course:", x, ",", "Students:", dict_[x])
    
new_dictionary = {x: dict_[x] for x in dict_}
new_dictionary["Fullstack"] = len(frontend) + len(backend)
print("New dict = ",new_dictionary)
