from datetime import datetime

class NetworkNode: 

    def __init__(self, ip):
        self.ip = ip
        self.heartBeat = 0
        self.failed = False 
        self.updateTime = datetime.now()

    
    def incrementHb(self):
        self.heartBeat += 1
        self.updateTime = datetime.now()

    def markAsFailed(self):
        self.failed = True
