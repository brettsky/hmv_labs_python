'''
Codename: levelx09
Mission: In this mission you will receive a string encrypted with ROT13, you must decode it and return the result.

'''


import socket
import codecs # we import the codecs module to encode and decode strings


HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx09')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)


        # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

        # Convert the string into a rot13 encoded string
    data_rot13 = codecs.encode(data_string, 'rot13')
    print(f"This is the string encoded in rot13:\n{data_rot13}")

    # Convert the string to bytes
    bytes_rot13 = data_rot13.encode('utf-8')
    print(f"This is the rot13 string converted to bytes:\n {bytes_rot13}")

        # Send the challenge back
    print('Sending challenge.')
    s.send(bytes_rot13)
    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)