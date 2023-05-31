# Advent of Code 2015 Day 19
# https://adventofcode.com/2015/day/19

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
testing = True
with open('day19.txt') as f:
    lst = list()
    lines = f.readlines()
    reps = dict()
    #print(lines)
    for s in lines[:-2]:
        s2 = s.split(' => ')
        #print(s2)
        reps[s2[0]] = s2[1][:-1]
    starting_str = lines[-1]
    print(reps)
    print(starting_str)

def replace(str1,str2,place):
    """Replacement of str1 into str2"""
    pass

def part1():
    output = set()
    for x in reps:
        if x in starting_str:
            output.add(starting_str.replace(x,reps[x],1))

def part2():
    pass

#print(part1())
#print(part2())
print("Time (secs):",time.time()-starting_time)