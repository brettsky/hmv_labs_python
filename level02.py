'''
Mission: In this mission you will receive a string and you must return the same string but converted to uppercase.

'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx02')

    print('Receiving challenge')
    data2 = s.recv(1024)

    print(data2)

    print('Sending challenge')
    s.send(data2.upper())

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)
