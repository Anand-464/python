class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
class employee(person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        
class part_time(person):
    def __init__(self, name, age, working_hour):
        super().__init__(name, age)
        self.working_hour = working_hour
        
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hour)
        
class consultant(employee,part_time):
    def __init__(self, name, age, employee_id, working_hour, project_name):
        part_time.__init__(self, name, age, working_hour)
        self.employee_id = employee_id
        self.project_name = project_name
        
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hour)
        print("Project Name:", self.project_name)

person1 = person("Alice", 25)
employee1 = employee("Bob", 30, "E101")
parttime1 = part_time("Charlie", 22, 20.5)
consultant1 = consultant("John", 35, "E123", 25.5, "ProjectX")

person1.show_details()
employee1.show_details()
parttime1.show_details()
consultant1.show_details()