web_develop = ["abhi", "john", "jane"]
data_science = ["alice", "bob", "asha"]
ui_ux_design = ["charlie", "diana", "peter"]

all_participants = [web_develop,data_science,ui_ux_design]
print(all_participants)

web_develop.append("hari")
print(web_develop)

data_science.insert(1,"akash")
print(data_science) 

ui_ux_design.pop()
print(ui_ux_design)

new_data_list = data_science.copy()
data_science.clear()
print("old list = ",data_science)
print("new list = ",new_data_list)

print(web_develop[:2])

name_len = [len(name) for name in new_data_list]
print("length = ",name_len)

if "asha" in web_develop or "asha" in new_data_list or "asha" in ui_ux_design:
    print("Asha is present")
else:
    print("Asha is absent")
    
tuple_ = (web_develop[0],new_data_list[0],ui_ux_design[0])
print(tuple_)