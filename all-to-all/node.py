import threading
import time
import socket
import os
from networknode import NetworkNode


ips = ['10.128.0.2', '10.128.0.3', '10.128.0.5', '10.128.0.6', '10.128.0.7']
nodes = []
refreshed_nodes = []

host = socket.gethostbyname(socket.gethostname())
ips.remove(host)

def populate_node_list():
    for ip in ips:
        nodes.append(NetworkNode(ip))
    refreshed_nodes = nodes
    
populate_node_list()

def validateNodes():
    while True:
        nodes = refreshed_nodes
        for node in nodes:
            if node.failed == True:
                print('Node with ip:' + node.ip + ' has failed')
                refreshed_nodes.remove(node)

def pingAll():
    while True:
        for node in nodes:
            print('Pinging: ' + node.ip)
            if os.system('ping -c 1 ' + node.ip + ' >/dev/null') == 0:
                node.incrementHb()
            else:
                node.markAsFailed()
            validateNodes()
        time.sleep(2)

pingAll()
            

        




