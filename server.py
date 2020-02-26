import socket,os

# Create a TCP/IP socket
sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Bind the socket to the port
sockTCP.bind(('0.0.0.0', 4466))  

sockTCP.listen(5)  

CONNECTION_LIST = []

while True:  
    print("Waiting for TCP Message...")
    connection,address = sockTCP.accept()  
    print("Client " + str(connection) + " connected.")
    CONNECTION_LIST.append(connection)
    buf = connection.recv(1024)  
    print ("Got message: " + str(buf))
    
    for con in CONNECTION_LIST:
        con.send(buf)
