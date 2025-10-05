import socket



'''
Mission: This mission is similar to the previous one, but adding a minimum of complexity :)
You will receive a string, you must return the same string and you will 
receive another string which you must also return.

'''

HOST = "temperance.hackmyvm.eu"
PORT = 9988


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #connecting to the host

    #receiving data sent from first challenge
    print('Receiving intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx01')
    

    print('Receiving challenge')
    data2 = s.recv(1024) 
    print(data2) #HMVTEACHING 

    print('Sending challenge')
    s.send(data2)
    
    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3) #NOOBSKILLZ

    print('Sending flag')
    s.send(data3)
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4) #HFlag: HMV{3ch03zlol}'



