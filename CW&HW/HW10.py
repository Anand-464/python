from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
    def account_age(self):
        return 2025 - self.account_year
    
    @abstractmethod
    def get_role(self):
        pass
        
class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Name:= {self.name},Account year:= {self.account_year}, Account age:= {self.account_age()}"

class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Name:= {self.name},Account year:= {self.account_year}, Account age:= {self.account_age()}"

admin = Admin("Aby",2001)     
guest = Guest("Akash", 2000)

print(admin)
print(guest)
