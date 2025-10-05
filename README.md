Python Labs from https://hackmyvm.eu/temperance



The following code can be repeated for everylevel 

it is used to connect to the server and receive the data. Challenge data will usually be stored in data2

import socket

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
