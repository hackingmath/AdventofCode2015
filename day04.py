# Thanks to geeksforgeeks.org/md5-hash-python/

import hashlib
import time

start = time.time()
#initializing string
n = 0
str1 = 'ckczppom'
while True:
    str2hash = str1+str(n)#'GeeksforGeeks'

    #encoding using encode()
    #then sending to md5()

    result = hashlib.md5(str2hash.encode())

    #printing the hex value
    #print("The hex equivalent of hash is")
    if result.hexdigest()[:6] == '000000':
        print("The number is", n)
        print(result.hexdigest())
        break
    n += 1
    # if n % 10000 == 0:
    #     print("n:",n)

print("Time:",time.time()-start)