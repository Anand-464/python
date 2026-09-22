try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    
    if name == "" or feedback == "":
        raise ValueError("Input empty")
    
    print("Thank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)
    
except ValueError as error:
    print("Error: ",error)

finally:
    print("Feedback completed")