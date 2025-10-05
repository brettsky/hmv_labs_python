

'''
Codename: levelx08
Mission: In this mission you will receive 2 numbers, you must return the result of adding both.
'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx08')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(data2)

    # we have to return the result of adding both numbers

    data_list = data2.split() # we split the string into a list
    print(f"This is the string converted to a list:\n{data_list}")

    int_list = [int(i) for i in data_list] # we convert the list items to integers
    print(f"This is the list items converted to integers:\n{int_list}")

    # Add the two numbers and save the result as a variable
    two_numbers_added = int_list[0] + int_list[1] # indexing the list to get the two numbers
    print(f"The result of the two numbers added together is {two_numbers_added}")


    string_two_numbers = str(two_numbers_added) # we convert the result to a string
    print(f"This is the result converted to string:\n {string_two_numbers}")


        # Convert the string to bytes
    bytes_two_numbers = string_two_numbers.encode('utf-8') # we convert the string to bytes because the server expects bytes
    print(f"This is the result converted to bytes:\n {bytes_two_numbers}")


        # Send the challenge back
    print('Sending challenge.') 
    s.send(bytes_two_numbers) # we send the result to the server

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024) # we receive the flag
    print(data4)
