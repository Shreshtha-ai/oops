# ─────────────────────────────────────────────
#  Multiple Inheritance – Smart Home Example
# ─────────────────────────────────────────────

class Device:
    def __init__(self,device_name,device_id,**kwargs):
        self.device_name = device_name
        self.device_id = device_id

    def device_status(self):
        print("Device is On")
    


class WifiEnabled(Device):
    def __init__(self,device_name,device_id,wifi_name,**kwargs):
        super().__init__(device_name,device_id,**kwargs)
        self.wifi_name = wifi_name

    def connect_wifi(self):
        print("Wifi connected to",self.wifi_name)

class VoiceControlled(Device):
    def __init__(self, device_name, device_id, assistant_name,**kwargs):
        super().__init__(device_name, device_id,**kwargs)        
        self.assistant_name = assistant_name

    def voice_command(self,command):
        print("Command received:", command)
        print("Assistant", self.assistant_name, "Executing")



class SmartSpeaker(WifiEnabled, VoiceControlled):
    def __init__(self, device_name, device_id, wifi_name, assistant_name):
        super().__init__(device_name,device_id,wifi_name = wifi_name,assistant_name = assistant_name)
        
        
    def display_info(self):
        print(f"  Device Name   : {self.device_name}")
        print(f"  Device ID     : {self.device_id}")
        print(f"  Wi-Fi Network : {self.wifi_name}")
        print(f"  Assistant     : {self.assistant_name}")


speaker = SmartSpeaker(
    device_name    = "Echo Pro",
    device_id      = "SP-2024",
    wifi_name      = "HomeNetwork_5G",
    assistant_name = "Alexa"
)

speaker.display_info()

speaker.device_status()
speaker.connect_wifi()
speaker.voice_command("Play lo-fi music")
print(SmartSpeaker.mro())



