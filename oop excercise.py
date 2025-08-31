class Vehicle:
    def __init__(self, name, max_speed, milage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
        self.capacity = capacity
    
    # def color(self, color="white"):
    #     self.color = color

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passangers"
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    # def seating_capacity(self):
    #     pass
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount
     
school_bus = Bus("School volvo", 180, 12, 50)
# print("Total Bus fare is:", school_bus.fare())
print(f"Total Bus fare is: {school_bus.fare()}")