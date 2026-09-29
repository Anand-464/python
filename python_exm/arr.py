arr = [{ "id": 1, "name": "rajesh"}, { "id": 2, "name": "rahul"}, { "id": 3, "name": "sruthi"}]

id = int(input("Enter an id: "))
for x in arr:
    if x["id"] == id:
        print(f"Name: {x['name']}")
        break
else:
    print("Id not found")
