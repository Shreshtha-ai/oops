class Vehicle:
    def __init__(self,vin,brand):
        self.vin = vin
        self.brand = brand
        print("Vehicle initiated")
    def start_engine(self):
        print(f"{self.brand} engine started")

class Electic(Vehicle):
    def __init__(self,vin,brand,battery_capacity,charge_level)
        super().__init__(vin,brand)
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level
    
    def charge(self):
        print(f"Charging{self.brand} battery")

class Autonomous(Vehicle):
    def __init__(self,vin,brand,software_version,sensor_count):
        super().__init__(vin,brand)
        self.software_version = software_version
        self.sensor_count = sensor_count

    def self_drivers(self):
        print(f"{self.brand} is driving autonomously")

class RoboTaxi(Electric,Autonomous):
   def __init__(self, vin, brand, battery_capacity, charge_level,
                 software_version, sensor_count, fare_per_km,
                 current_passenger):

        super().__init__(vin, brand, battery_capacity, charge_level,
                         software_version, sensor_count)

        self.fare_per_km = fare_per_km
        self.current_passenger = current_passenger
    
    def start_engine(self):
        print("vin:",self.vin)
        self.charge()
        self.self_drivers()

        
       
    
    

        
    
    
