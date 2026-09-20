class Vehicle:
    def __init__(self,vehicle_number,model,**kwargs):
        self.vehicle_number = vehicle_number
        self.model = model
    
    def vehicle_info(self):
        print("Vehical number:",self.vehicle_number)
        print("Model: ",self.model)

class ElectricVehicle(Vehicle):
    def __init__(self,vehicle_number,model,battery_capacity,**kwargs):
        super().__init__(vehicle_number,model,**kwargs)
        self.battery_capacity = battery_capacity
    
    def battery_info(self):
        print(self.battery_capacity)

class GPS(Vehicle):
    def __init__(self,vehicle_number,model,latitude,longitude,**kwargs):
        super().__init__(vehicle_number,model,**kwargs)
        self.latitude = latitude
        self.longitude = longitude
    
    def location_info(self):
        print(self.latitude,self.longitude)

class SmartCar(ElectricVehicle, GPS):
    def __init__(self,vehicle_number,model,battery_capacity,latitude,longitude):
        super().__init__(vehicle_number,model,battery_capacity = battery_capacity,latitude = latitude,longitude = longitude)
        
    def vehicle_info(self):
        super().vehicle_info()
        self.battery_info()
        self.location_info()


s1 = SmartCar("MH14AB1234","ModelS",100,19.208,72.8777)
s1.vehicle_info()
print(SmartCar.mro())



    

