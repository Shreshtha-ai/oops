class Media:
    def __init__(self,title,creator,duration):
        self.title = title
        self.creator = creator
        self.duration = duration
    
    def play(self):
        print("Playing media file")
    
class Video(Media):
    def __init__(self,title,creator,duration,resolution, frame_rate):
        super().__init__(title,creator,duration)
        self.resolution = resolution
        self.frame_rate = frame_rate
    
    def play(self):
        print("Playing video file")

class Podcast(Media):
    def __init__(self,title,creator,duration,episod_number, category):
        super().__init__(title,creator,duration)
        self.episod_number = episod_number
        self.category = category
    
    def play(self):
        print("Playing podcast")


v1 = Video("PKD", "MVS", 200, "1080p", "30fps")
print(v1.title)
print(v1.duration)
print(v1.resolution)
print(v1.frame_rate)
v1.play()

p1 = Podcast("PKD", "MVS", 200, 1,"Science")
print(p1.title)
print(p1.duration)
print(p1.category)
print(p1.episod_number)
p1.play()

