class Building:
    def __init__(self,Building_ID,Building_Name,Energy_consumption):
        self.Building_ID = Building_ID
        self.Building_Name = Building_Name
        self.__Energy_consumption = Energy_consumption

    def get_energy(self):
        return self.__Energy_consumption
    
    def set_energy(self,new_energy):
        if new_energy>0:
            self.__Energy_consumption = new_energy
        else:
            print("invalid energy")
    
class SmartBuilding(Building):
    def __init__(self,Building_ID,Building_Name,Energy_consumption,Security_Level):
        super().__init__(Building_ID,Building_Name,Energy_consumption)
        self.__Security_Level = Security_Level

    def calculate_bill(self,rate):
        return self.get_energy()*rate

class IndustrialBuilding(SmartBuilding):
    def __init__(self,Building_ID,Building_Name,Energy_consumption,Security_Level,Industry_Type):
        super().__init__(Building_ID,Building_Name,Energy_consumption,Security_Level)
        self.Industry_Type = Industry_Type
    
    def calculate_bill(self,rate):
        return self.get_energy()*(rate+rate*0.2)

s1 = SmartBuilding(1,"abc",1250,2)
print(s1.calculate_bill(5)) 
i1 = IndustrialBuilding(1,"abc",100,2,"heavy")
print(i1.calculate_bill(5))

print(isinstance(i1,IndustrialBuilding))
print(issubclass(IndustrialBuilding,SmartBuilding))

        
        
        