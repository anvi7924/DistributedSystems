# Save as client.py
# Message Sender
import os
from socket import *
import sys
import time

host = "10.0.0.13" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:

	#send data
    data = raw_input("Enter message to send or type 'exit': ")
    start = time.time()
    UDPSock.sendto(data, addr)
    if data == "exit":
        break

    #receive response
   	print >>sys.stderr, 'waiting to receive'
    data, server = UDPSock.recvfrom(4096)
    end = time.time()
    print >>sys.stderr, 'received "%s"' % data
    print('start', start)
    print('end', end)


UDPSock.close()
os._exit(0)