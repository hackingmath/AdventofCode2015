# Advent of Code 2015 Day 23
# https://adventofcode.com/2015/day/23

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day23.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def part1(testing=False):
    a,b = 1,0
    place = 0
    while place < len(lines):
        print("place:",place)
        instr = lines[place]
        instr = instr.split(' ')
        #print(instr)
        if instr[0] == 'jio':
            if a == 1:
                place += int(instr[2].strip("+"))
            else:
                place += 1
        elif instr[0] == 'jie':
            if a % 2 == 0:
                place += int(instr[2].strip("+"))
            else:
                place += 1
        elif instr[0] == 'jmp':
            if instr[1][0] == '+':
                place += int(instr[1].strip("+"))
            else:
                place -= int(instr[1][1:])
        elif instr[0] == 'inc':
            if instr[1][0] == 'a':
                a += 1
            else:
                b += 1
            place += 1
        elif instr[0] == 'tpl':
            if instr[1][0] == 'a':
                a *= 3
            else:
                b *= 3
            place += 1
        elif instr[0] == 'hlf':
            a /= 2
            place += 1
    print("a,b:",a,b)

def part2():
    pass

print(part1())
#print(part2())
print("Time (secs):",time.time()-starting_time)