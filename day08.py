# Advent of Code 2020 Day 8
# https://adventofcode.com/2020/day/8

import time

starting_time = time.time()

with open('day08.txt') as f:
    print("Part 1:",sum(len(_) - 1 - len(eval(_)) for _ in f))
    # lst = list()
    # lines = f.readlines()
    # lst.append(lines)

#print(lines)

escapes = ['\\','\"',"\'"]
def nums(str,testing = False):
    """Calculates the number of characters of code
    minus the number of characters in the string"""
    #This calculates characters in the string
    characters_in_string = len(str) - 2
    if testing:
        print("chars:",str,characters_in_string)
    #calculate  characters of code
    length = characters_in_string #+ 2 #double quotes
    if escapes[0] in str:
        length += str.count(escapes[0])
        if testing:
            print("\\",str.count(escapes[0]),"length:",length)
    if escapes[1] in str:
        length += str.count(escapes[1])
        if testing:
            print('\"',str.count(escapes[1]),"length:",length)
    if escapes[2] in str:
        length += 3*str.count(escapes[2])
        if testing:
            print("\\x", str.count(escapes[2]),"length:",length)
    return length - characters_in_string

test1 = ['""','"abc"','"aaa\"aaa"','"\x27"']

def part1(f):
    print(sum(len(_) - 1 - len(eval(_)) for _ in f))

#part1(test1)

# total = 0
# for str in test1:
#     total += nums(str,True)
# print("total",total) #1485 too high. 
print("Time (secs):",time.time()-starting_time)