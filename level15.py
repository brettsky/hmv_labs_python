'''
Codename: levelx15
Mission: In this mission you receive a series of numbers, you must return what the next number in the series would be.

'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx15" to choose the level
    s.send(b'levelx15')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

    # Convert the string into a list of numbers
    number_list = list(map(int, data_string.split()))
    print(f"This is the string converted to a list of numbers:\n{number_list}")

    # Calculate the next number in the series
    # Assuming it's an arithmetic series, we find the difference between the last two numbers
    difference = number_list[-1] - number_list[-2]
    next_number = number_list[-1] + difference
    print(f"This is the next number in the series:\n{next_number}")

    # Convert the next number to bytes
    bytes = str(next_number).encode('utf-8')
    print(f"This is the next number converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    flag = s.recv(1024)
    print(flag)