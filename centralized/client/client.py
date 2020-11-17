import socket
import time

server_ip = '10.128.0.2'
server_port = 80

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created")
except socket.error as err: 
    print("socket creation failed with error %s" %err)

heartBeat = 0
s.connect((server_ip, server_port))
while True:
    
    heartBeat += 1
    
    s.send(bytes([heartBeat]))
    print("Sent heartbeat number: " + str(heartBeat))

    time.sleep(5)

