# Advent of Code 2015 Day 10
# https://adventofcode.com/2015/day/10

import time

starting_time = time.time()
pinput = '1113222113'
testinput = '1'
N = 5

def transform(string):
    place = 1
    output = ""
    digit = string[0]
    run = 0
    for i,v in enumerate(string):
        if v == digit:
            run += 1
            if i == len(string) - 1:
                output += str(run) + digit
        else:
            output += str(run)+digit
            run = 1
            digit = string[i]
            if i == len(string) - 1:
                output += str(run) + digit
    return output

for i in range(50):
    pinput = transform(pinput)
print(len(pinput))
#print(transform('123'))

print("Time (secs):",time.time()-starting_time)