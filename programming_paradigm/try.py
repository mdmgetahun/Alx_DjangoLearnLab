class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def bark(self):
        return (f"{self.name} who is {self.age} says 'Arf'")
    
dog1 = Dog("Bolt", 2)
print(dog1.bark())
