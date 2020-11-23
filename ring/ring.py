import os
import sys
import time

node_ip = sys.argv[1]

while True:
    print('Pinging: ' + node_ip)
    if not(os.system('ping -c 1 ' + node_ip + ' >/dev/null') == 0):
        print('Node failed: ' + node_ip)
    time.sleep(2.5)