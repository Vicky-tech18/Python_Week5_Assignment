#  Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life # Private (encapsulation)
    
    def show_info(self):
        print(f"{self.brand} {self.model} - Battery: {self.__battery_life}%")

#   Child Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life,) #Inherit from smartphone
        self.cooling_system = cooling_system
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling!")

phone1 = Smartphone("Apple", "iphone 15", 80)
phone1.show_info()

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 60, "Liquid Cooling")
gaming_phone.show_info()
gaming_phone.play_game("PUBG Mobile")

# Polymorphism
class Vehicle:
    def move(self):
        raise NotADirectoryError("This method should be overridden!")
class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water...")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each would end on its own move() method