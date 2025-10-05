import base64
import socket

'''
Codename: levelx03
Mission: In this mission you will receive a string in base64, you must do the decode and return the result. 
'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    
    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx03')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)

    #data2 is stored in base64  "RGFWRHRCQ1pYYk1oZlJtWVhORU9scWVacw=="

    print('Sending challenge')
    decoded_data = base64.b64decode(data2) #using base64 to decode the data sent from the server

    print('Receiving flag')
    print(decoded_data)

    s.send(decoded_data)

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)