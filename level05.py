

'''
# EN
Codename: levelx05
Mission: In this mission you will receive a string and you must return the last 5 chars.


'''


    
    # We have to return the last 5 chars of the string "BWGyiKQKjmsHZSUgjZjhCqReE"

    # we will also use string slicing to get the last 5 chars

    data2_last_5_chars = data2[-5:]

    print(data2_last_5_chars)

    print('Sending challenge')
    s.send(data2_last_5_chars)

    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)
