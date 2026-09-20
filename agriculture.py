class farm:
    def __init__(self,farm_id,location,**kwargs):
        self.farm_id = farm_id
        self.location = location

    def farm_info(self):
        print("Farm ID:",self.farm_id)
        print("Location:",self.location)

class WeatherSensor(farm):
    def __init__(self,farm_id,location,temperature,humidity,**kwargs):
        super().__init__(farm_id,location,**kwargs)
        self.temperature = temperature
        self.humidity = humidity

    def weather_data(self):
        print(self.temperature,self.humidity)

class SoilSensor(farm):
    def __init__(self,farm_id,location,soil_moisture,soil_ph):
        super().__init__(farm_id,location)
        self.soil_moisture = soil_moisture
        self.soil_ph = soil_ph

    def soil_data(self):
        print(self.soil_moisture,self.soil_ph)


class SmartFarm(WeatherSensor,SoilSensor):
    def __init__(self,farm_id,location,temperature,humidity,soil_moisture,soil_ph):
        super().__init__(farm_id,location,temperature = temperature,humidity = humidity,soil_moisture = soil_moisture,soil_ph = soil_ph)

    def display_info(self):
        self.farm_info()
        self.weather_data()
        self.soil_data()

sf1 = SmartFarm(farm_id="F01",location = "Pune", temperature = 25, humidity = 60, soil_moisture = 40, soil_ph = 6.5)
sf1.display_info()
print(SmartFarm.mro())

    
        