import time
import os

class Timer:
    
    def __init__(self, seconds=0, minutes=0, hours=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        
    def __repr__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
    
    def increments(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        
    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.increments()
            time.sleep(1)
            
timer1 = Timer()

timer1.start()
    