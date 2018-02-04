# hello-world
getting started tutorial - edited line in new branch
this is a new line added in a new branch 

Use the script from Octave command prompt like this 
iq=convertToIQ('fileNameToRead', 'fileNameToWrite');

TCP server worked! 
Use nc to send file like this 
nc -w1 127.0.0.1 < fileName

use python script like this: 

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 52002
MESSAGE = "Hello, from python!\n"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

sudo apt-get install bless ile hex editor kurulabilir. 

