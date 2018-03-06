import socket
import subprocess
import sys
import datetime

subprocess.call('clear',shell=True)

remoteserver = input("Enter a host to scan:")
remoteIP = socket.gethostbyname(remoteserver)

print("Scanning %s"%remoteIP)

#t1 = datetime.now()

try:
    for port in range(1,443):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteIP,port))
        if result == 0:
            print("Port{}:     Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("You hit Ctrl+C")
except socket.error:
    print("Couldn't connect to server")
    sys.exit()