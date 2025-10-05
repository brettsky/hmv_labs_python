'''

# EN
Codename: levelx12
Mission: In this mission you receive a string and a number, you must return the string repeated n number of times.
'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Receiving intro')
    data = s.recv(1024)

    print(data)

    s.send(b'levelx12')

    print('Receiving challenge')
    data2 = s.recv(1024)

    print(data2)

    data2_string = data2.decode('utf-8')
    print(data2_string)

    data2_list = data2_string.split()
    print(data2_list)

 

    target_string = data2_list[0]
    print(target_string)

    target_number = int(data2_list[1])
    print(target_number)


    multiplied_string = target_string * target_number

    print(multiplied_string)

    # send the multiplied string to the server as bytes

    multiplied_string_bytes = multiplied_string.encode('utf-8')
    print(multiplied_string_bytes)

    s.send(multiplied_string_bytes)

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)
  
        