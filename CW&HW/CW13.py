item = input("Enter the item: =")
f = open("items.txt","a")
f.write(item + "\n")
f.close()

f = open("items.txt", "r")
print("\nItem list: ")

for x in f:
    print(x.strip())
f.close()

