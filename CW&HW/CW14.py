import random
import math

names = input("Enter names:- ").split(",")

no_dupes = []
for x in names:
    x = x.strip()
    if x not in no_dupes:
        no_dupes.append(x)
print("Unique names:- ", no_dupes)

random_name = random.choice(no_dupes)
print("Random name:- ", random_name)

def reverse(random_name):
    random_name = random_name[::-1]
    return random_name

reversed_name = reverse(random_name)
print("Reversed name:- ", reversed_name)

total = len(no_dupes)
print("Total unique names:- ", total)
final_num = math.sqrt(total)
print("Sqrt of unique name:- ", final_num)
print("Rounded sqrt:- ", round(final_num))
