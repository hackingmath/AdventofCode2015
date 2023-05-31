# Advent of Code 2015 Day 17
# https://adventofcode.com/2015/day/17

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
testing = True
with open('day17.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [int(x) for x in lines]
    #print(lines)

def part1():
    ways = list()
    for i in range(4,20):
        oneway = combinations(lines,i)
        for w in oneway:
            if sum(w) == 150:
                ways.append(w)
    return len(ways)

def part2():
    ways = dict()
    for i in range(3,20):
        oneway = combinations(lines,i)
        for w in oneway:
            if sum(w) == 150:
                if i not in ways:
                    ways[i] = 1
                else:
                    ways[i] += 1
    return ways

#print(part1())
print(part2())
print("Time (secs):",time.time()-starting_time)