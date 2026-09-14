attendance = [18, 20, 19, 15, 21]
class_full = 0
total=0

for x in attendance:
    if x>=20:
        print("class full")
        class_full +=1
    else:
        print("not full")
    total +=x 
print("Full classes = ",class_full)
print("Total = ",total)