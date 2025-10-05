'''
Codename: levelx16
Mission: In this mission you receive a png encoded in base64, you must decode it and return 
the size in pixels of its width and height

'''

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

    # Send "levelx16" to choose the level
    s.send(b'levelx16')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string: {data_string}")

    # Decode the base64 string into bytes
    image_bytes = base64.b64decode(data_string)
    print(f"This is the image decoded from base64 into bytes: {image_bytes}...")

    # The width and height of a PNG image are stored in bytes 16-23
    width = int.from_bytes(image_bytes[16:20], byteorder='big')
    height = int.from_bytes(image_bytes[20:24], byteorder='big')
    print(f"This is the width and height of the image: {width}x{height}")

    # Create the response string in the format "widthxheight"
    response_string = f"{width}x{height}"
    
    # Convert the response string to bytes
    response_bytes = response_string.encode('utf-8')
    print(f"This is the response string converted to bytes: {response_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(response_bytes)

    # Receive the flag
    print('Receiving flag')
    flag = s.recv(1024)
    print(flag)