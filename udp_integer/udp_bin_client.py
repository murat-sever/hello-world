
import binascii
import socket
import struct
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5001)
#sock.connect(server_address)

#values = (1, 'ab', 2.7)
#packer = struct.Struct('I 2s f')
values = (1,2,3,4)
packer = struct.Struct('I I I I')
packed_data = packer.pack(*values)

try:
    
    # Send data
    print >>sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
    sock.sendto(packed_data, server_address)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()


