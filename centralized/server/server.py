import socket
import threading
import time
from datetime import datetime

host = socket.gethostbyname(socket.gethostname())
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen()
print('Listening on: ' + host)
hbs = {}

def handle_client(conn, addr):
    while conn.recv(1024):
        print("Received")
        hbs[addr[0]] = datetime.now()

    conn.close()

def validate_heartbeats():
    while True:
        time.sleep(2)
        for key in hbs:
            if (datetime.now() - hbs[key]).total_seconds() > 10 and hbs[key] != 0:
                hbs[key] = 0
                print('Failed connection detected for: ' + key)

validation_thread = threading.Thread(target=validate_heartbeats)
validation_thread.start()

while True:
    conn, addr = s.accept()
    print('New connection: ' + addr[0])
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()