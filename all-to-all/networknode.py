from datetime import datetime

class NetworkNode: 

    def __init__(self, ip):
        self.ip = ip
        self.heartBeat = 0
        self.failed = False 
        self.updateTime = datetime.now()

    
    def incrementHb(self, heartBeat):
        self.heartBeat = heartBeat
        self.updateTime = datetIme.now()

    def markAsFailed(self):
        self.failed = True
