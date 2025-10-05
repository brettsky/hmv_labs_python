import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message 
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx00" to choose the level 
    s.send(b'levelx00')

    # Receive the challenge 
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Send the challenge solved 
    print('Sending challenge')
    s.send(data2)

    # Receive the flag  
    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)

