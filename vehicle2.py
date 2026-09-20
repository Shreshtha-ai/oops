class Vehicle:
    def __init__(self,Vehicle_Number,Vehicle_Name):
        self.Vehicle_Number = Vehicle_Number
        self.Vehicle_Name = Vehicle_Name
    
    def maintenance_cost(self):
        return 5000

class ElectricVehicle(Vehicle):
    def __init__(self,Vehicle_Name,Vehicle_Number,Battery_Capacity):
        super().__init__(Vehicle_Number,Vehicle_Name)
        self.Battery_Capacity = Battery_Capacity
    
    def maintenance_cost(self):
        return (self.Battery_Capacity)*100
    

e = ElectricVehicle("EV12","MH14AB3456",500)
v = Vehicle("V12","MH14AB3456")
print(e.maintenance_cost())
print(v.maintenance_cost())
    
    
        

    