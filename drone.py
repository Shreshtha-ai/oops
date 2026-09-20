class Drone:
    def __init__(self,drone_id,model,**kwargs):
        self.drone_id = drone_id
        self.model = model

    def drone_info(self):
        print(self.drone_id,self.model)

class CameraSystem(Drone):
    def __init__(self,drone_id,model,camera_resolution,**kwargs):
        super().__init__(drone_id,model,**kwargs)
        self.camera_resolution = camera_resolution

    def capture_image(self):
        print("Image captured at:",self.camera_resolution)

class NavigationSystem(Drone):
    def __init__(self, drone_id,model,current_location,**kwargs):
        super().__init__(drone_id,model,**kwargs)
        self.current_location = current_location
    
    def navigate(self):
        print("Drone is navigating to destination")

class AutonomousDrone(CameraSystem,NavigationSystem):
    def __init__(self,drone_id,model,camera_resolution,current_location):
        super().__init__(drone_id,model,camera_resolution = camera_resolution,current_location = current_location)
    
    def perform_mission(self):
        print("Drone is starting mission")
        self.navigate()
        self.capture_image()
        print("Mission complete")


drone = AutonomousDrone("D101", "DJI", "4K", "Delhi")

drone.drone_info()
drone.perform_mission()

print(AutonomousDrone.mro())
        
    


        
    