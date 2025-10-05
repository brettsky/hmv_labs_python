'''
Codename: levelx14
Mission: In this mission you receive a string and a character, you must return the number 
of times the character is repeated in the string

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

    # Send "levelx13" to choose the level
    s.send(b'levelx14')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")


    # we will use the count function to count the number of times the character is in the string
    # the character is always the last character in the string
    char_to_count = data_string[-1]
    print(f"This is the character to count:\n{char_to_count}")

    # the string is everything except the last character
    string_to_search = data_string[:-2]
    print(f"This is the string to search:\n{string_to_search}")
    # count the number of times the character is in the string
    count = string_to_search.count(char_to_count)
    print(f"This is the count of the character in the string:\n{count}")

    # Convert the count to bytes
    bytes = str(count).encode('utf-8')


    print(f"This is the count converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)
    # Receive the flag
    print('Receiving flag')
    flag = s.recv(1024)
    print(flag)