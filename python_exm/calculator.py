class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class oper(calc):           
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        return self.x / self.y
    
x = int(input("first num: "))
y = int(input("second num: "))
action = input("enter operation: ")

obj = oper(x, y)

if action == "+":
    print("Sum is: ", obj.add())
elif action == "-":
    print("Difference is: ", obj.subtract())
elif action == "*":
    print("Product is: ", obj.multiply())
elif action == "/":
    if x == 0 or y == 0:
        print("Division by zero is not allowed")
    else:
        print("Division is: ", obj.divide())