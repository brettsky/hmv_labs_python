'''

Codename: levelx07
Mission: In this mission you will receive a string in hexadecimal format, you must return it converted to ascii.

'''


import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)


    s.send(b'levelx07')

    print('Receiving challenge')
    data2 = s.recv(1024)
    
    print(data2)

    data2_hex = data2.decode('utf-8')

    hex_string = data2_hex
    print(hex_string)

    bytes_object = bytes.fromhex(hex_string)
    print(bytes_object)

    ascii_string = bytes_object.decode('ascii')
    print(ascii_string)

    print('Sending challenge')
    ascii_bytes = ascii_string.encode('ascii')
    print(ascii_bytes)
    s.send(ascii_bytes)

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)


