from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year
    def calc_yr(self):
        return 2025 - self.joining_year
    
    @abstractmethod
    def role(self):
        pass
    def __str__(self):
        return f"Name: {self.name}, Role: {self.role()}, Years on platform: {self.calc_yr()}"
    
class Customer(User):
    def role(self):
        return "Customer"
    
class Vendor(User):
    def role(self):
        return "Vendor"
    
customer = Customer("Aby",2001)     
vendor = Vendor("Akash", 2000)

print(customer)
print(vendor)
