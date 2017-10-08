import socket
import sys
import json

HOST, PORT = "192.168.1.71", 9999

m ='{"id": 2, "name": "abc"}'

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(m)

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     {}".format(m))
print("Received: {}".format(received))