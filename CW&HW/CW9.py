class Vehicle:
    def __init__(self, _vehicle_id,  _base_rate):
        self._vehicle_id = _vehicle_id
        self._base_rate =  _base_rate
    def display_details(self):
        print(f"Vehicle ID id {self._vehicle_id}")
        print(f"Base rate {self._base_rate}")
    def rental_charge(self):
        return 0.0
    
class Car(Vehicle):
    def __init__(self, _vehicle_id, _base_rate, num_seat):
        super().__init__(_vehicle_id, _base_rate)
        self.num_seat = num_seat
    def rental_charge(self):
        return self._base_rate * self.num_seat
    
class Bike(Vehicle):
    def __init__(self, _vehicle_id, _base_rate, bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type = bike_type
    def rental_charge(self):
        return self._base_rate * 0.5
    
def calculate_rental(Vehicle):
    return Vehicle.rental_charge()

car1 = Car("CAR001", 100.00, 4)
bike1 = Bike("BIKE001", 50.00, "Motorcycle")

for x in (car1, bike1):  
    Vehicle.display_details(x)
    print("Rental Charge:", calculate_rental(x))