fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
beverages = ["water", "juice", "soda"]

fruits.append("lemon")
print(fruits)

vegetables.insert(1,"potato")
print(vegetables)

beverages.pop()
print(beverages)

inventory = [fruits, vegetables, beverages]
print(inventory)

print(fruits[0:2])
print(vegetables[-1])

fruit_lengths = [len(x) for x in fruits]
print("length is = ",fruit_lengths)

if "water" in beverages:
    print("water is present")
else:
    print("water is absent")

tuple_ = (fruits[0],vegetables[0],beverages[0])
print(tuple_)