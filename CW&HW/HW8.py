class employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def display(self):
        print("name", self.name)
        print("role", self.role)
        
class trainer(employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization
    def display(self):
        print("name", self.name)
        print("role", self.role)
        print("specialization", self.specialization)
        
class yoga_instructor(employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style
    def display(self):
        print("name", self.name)
        print("role", self.role)
        print("yoga style", self.yoga_style)
        
class multi_trainer(trainer, yoga_instructor):
    def __init__(self, name, role, specialization, yoga_style):
        employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style
    def display(self):
        print("name", self.name)
        print("role", self.role)
        print("specialization", self.specialization)
        print("yoga style", self.yoga_style)
       
employee1 = employee("Alice", "Manager")
trainer1 = trainer("Bob", "Trainer", "E101")
yoga_instructor1 = yoga_instructor("Charlie", "Yoga Instructor", "Hatha")
multi_trainer1 = multi_trainer("David", "Multi-Trainer", "Fitness", "Vinyasa")

employee1.display()
trainer1.display()
yoga_instructor1.display()
multi_trainer1.display()