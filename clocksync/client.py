
import socket
import sys
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.217.2.167', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    import time
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    start = time.time()
    data, server = sock.recvfrom(4096)
    end = time.time()
    print >>sys.stderr, 'received "%s"' % data
    print('start', start)
    print('end', end)
    # print('latency', latency)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()