'''

Codename: levelx04
Mission: In this mission you will receive a string and you must return it in reverse.

'''

import socket


HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx04')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)
   # string to reverse is   uReYZFMaQcZadmApikxnlzXmM

 #using string slicing to reverse the string

    data2_reversed = data2[::-1]

    print(data2_reversed)

    print('Sending challenge')
    s.send(data2_reversed)

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)
