import re

try:
    title = input("Enter book title: ")
    year = input("Enter book year: ")
    
    if not title.replace(" ","").isalpha():
        raise ValueError("Wrong title")
    
    if not year.isdigit() or len(year)!= 4 or not re.match(r"^(19|20)\d{2}$",year):
        raise ValueError("Wrong year")
    
except ValueError as error:
    print("Error: ", error)
    
finally:
    print("Input processed")