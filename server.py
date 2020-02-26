import socket,os

# Create a TCP/IP socket
sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Bind the socket to the port
sockTCP.bind(('0.0.0.0', 4466))  

sockTCP.listen(5)  


while True:  
    print("Waiting for TCP Message...")
    connection,address = sockTCP.accept()  
    buf = connection.recv(1024)  
    print ("Got message: " + str(buf))
    connection.broadcast(buf)
    #connection.close()