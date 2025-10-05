'''
Codename: levelx11
Mission: In this mission you will receive a string in Morse code, you must decode it and return it.

'''

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx11')

    print('Receiving challenge')
    data2 = s.recv(1024)
    print(f"This is the challenge: in bytes\n{data2}")

    data2_string = data2.decode('utf-8')
    print(f"This is the challenge: in string\n{data2_string}")

    #to decode the morse code we will use a dictionary that maps the morse code to the letter
    MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' ', '.-.-.-': '.', '--..--': ',', '..--..': '?',
    '-.-.--': '!', '---...': ':', '-....-': '-', '.-..-.': '"',
    '.--.-.': '@', 
}


    #decode the morse code
    decoded_string = ''.join(MORSE_CODE_DICT.get(code) for code in data2_string.split(' ')) #Splits the Morse code message into individual symbols, looks up each symbol in the Morse code dictionary, replaces it with its corresponding letter (or a space), and joins all those letters together into one readable string.
    print(f"This is the decoded string:\n{decoded_string}")

    #convert the decoded string to bytes
    decoded_string_bytes = decoded_string.encode('utf-8')
    print(f"This is the decoded string converted to bytes:\n{decoded_string_bytes}")

    #send the decoded string to the server
    s.send(decoded_string_bytes)

    #receive the flag
    data3 = s.recv(1024)
    print(f"This is the flag:\n{data3}")


