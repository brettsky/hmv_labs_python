'''
Codename: levelx17
Mission: In this mission you receive a 1 pixel png encoded in base64, you must decode it and return the last RGBA value.

'''

import socket

import base64

import io
import PIL
from PIL import Image

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx17" to choose the level
    s.send(b'levelx17')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string: {data_string}")

    # Decode the base64 string into bytes
    png_bytes = base64.b64decode(data_string)
    print(f"This is the image decoded from base64 into bytes: {png_bytes}")

    png_image = Image.open(io.BytesIO(png_bytes))
    png_image = png_image.convert("RGBA")
    width, height = png_image.size
    print(f"These are the dimensions of the PNG image:\n{width}, {height}")

    #RBGA value of the last pixel
    rbga_value = png_image.getpixel((width-1, height-1))
    print(f"This is the RGBA value of the last pixel:\n{rbga_value}")

    last__value = rbga_value[-1]
    print(f"This is the last value of the RGBA value:\n{last__value}")


    # convert the last value to a string and then to bytes

    value_string = str(last__value)
    value_bytes = value_string.encode('utf-8')
    print(f"This is the last value converted to bytes:\n{value_bytes}")
    # Send the challenge back
    print('Sending challenge.')
    s.send(value_bytes) 
    # Receive the flag
    print('Receiving flag')
    flag = s.recv(1024)
    print(flag)


