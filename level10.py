'''
Codename: levelx10
Mission: In this mission you will receive numbers separated by spaces, you must return them in order from 
smallest to largest and without separating them with spaces.

'''
import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx10')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

        # Convert the string into a list of objects
    data_list = data_string.split()
    print(f"This is the string converted to a list:\n{data_list}")


    # Sort the list
    data_list.sort()
    print(f"This is the sorted list:\n {data_list}")



    # Convert the list to a string and concatenate
    concatenated_string = "".join(data_list)
    print(f"This is the list as a string concatenated blob:\n{concatenated_string}")


        # Convert the string to bytes
    bytes = concatenated_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")


        # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
    
