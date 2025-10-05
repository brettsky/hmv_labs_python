'''
Codename: levelx06
Mission: In this mission you will receive a string and you must return its length. (as string, not as int).
'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx06')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)# b'PxYldfdjpHbquOtToIWNYPscWXGUPxjhJSffOsxuNcQNYwbEcqDyFE'

    data_string = data2.decode('utf-8') # we have to decode from bytes to string


    string_length = str(len(data_string))


    length_bytes = string_length.encode("utf-8") # we have to encode from string to bytes because the server expects bytes

    print(length_bytes)
    s.send(length_bytes) # we are sending the length of the string

    data4 = s.recv(1024)
    print(data4)