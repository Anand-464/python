class Account:
    def __init__(self, _name, _balance):
        self._name = _name
        self._balance = _balance
    def __add__(self, other):
        return self._balance + other._balance
        
class SavingsAccount(Account):
    def __init__(self, _name, _balance):
        super().__init__(_name, _balance)
    def calculate_interest(self):
        return self._balance * 0.05

class CurrentAccount(Account):
    def __init__(self, _name, _balance):
        super().__init__(_name, _balance)
    def calculate_interest(self):
        return self._balance * 0.02
    
savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

for account in (savings, current):
    print("Name:", account._name)
    print("Balance:", account._balance)
    print("Interest:", account.calculate_interest())
    print()

print("Total Balance:", savings + current)
