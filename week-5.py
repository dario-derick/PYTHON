#Activity 1

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived Class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}")

    def charge(self):
        print(f"🔋 {self.device_info()} is charging...")

    def check_specs(self):
        print(f"📱 {self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh")


# Creating objects
phone1 = Smartphone("Apple", "iPhone 14", 256, 3200)
phone2 = Smartphone("Samsung", "Galaxy S23", 512, 4000)

# Testing methods
phone1.make_call("123-456-789")
phone1.check_specs()
phone2.charge()


#Activity 2
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on the water.")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Same method name, different behavior
