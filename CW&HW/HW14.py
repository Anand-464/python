import random
import math

names = input("Enter the names:- ").split(",")

no_dupes = []
for x in names:
    x = x.strip()
    if x not in no_dupes:
        no_dupes.append(x)
print("Unique names:- ", no_dupes)

random.shuffle(no_dupes)

winner = random.sample(no_dupes, 2)
print("Winners:- ", winner)

def reverse(name):
    return name[::-1]

reversed_name1 = reverse(winner[0])
reversed_name2 = reverse(winner[1])
print("Reversed winner 1:- ", reversed_name1)
print("Reversed winner 2:- ", reversed_name2)

total = len(no_dupes)
print("Total unique names:- ", total)
final_num = math.sqrt(total)
print("Sqrt of unique name:- ", final_num)
print("Rounded sqrt:- ", round(final_num))