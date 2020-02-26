import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 4467)
print('starting server on ' + str(server_address))
sock.bind(server_address)

while True:
    print('waiting to receive message')
    data, address = sock.recvfrom(4096)
    
    print('received bytes')
    print(data)
    
    if data:
        sent = sock.sendto(data, address)
        print('sent bytes back')