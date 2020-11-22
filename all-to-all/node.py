import threading
import time
import socket
import os
from networknode import NetworkNode


ips = ['10.128.0.2', '10.128.0.3', '10.128.0.5', '10.128.0.6', '10.128.0.7']
nodes = []

host = socket.gethostbyname(socket.gethostname())
print(host)
ips.remove(host)

def populate_node_list():
    for ip in ips:
        nodes.append(NetworkNode(ip))

populate_node_list()

def pingAll():
    while True:
        for node in nodes:
            if os.system('ping -c 1 ' + node.ip) == 0:
                node.incrementHb()
        time.sleep(2)

def validateNodes():
    time.sleep(5)
    while True:
        for node in nodes:
            if node.failed == False and (datetime.now() - hbs[key]).total_seconds() > 10:
                node.failed = True
                print('Node with ip:' + node.ip + 'has failed')


threading.Thread(target = pingAll).run()
threading.Thread(target = validateNodes).run()
            

        




