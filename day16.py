# Advent of Code 2015 Day 16
# https://adventofcode.com/2015/day/16

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
testing = True
with open('day16.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.split(" ") for x in lines]
    print(lines)
    sue_list = list()
    for s in lines:
        this_sue = {s[2][:-1]:int(s[3][:-1]),s[4][:-1]:int(s[5][:-1]),s[6][:-1]:int(s[7][:-1])}
        sue_list.append(this_sue)
    print(sue_list)

target_sue = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}
def part1():
    for n,sue in enumerate(sue_list):
        matches = 0
        for a in sue:
            if sue[a] == target_sue[a]:
                matches += 1
            if matches == 3:
                print("Sue #",n+1)

def part2():
    """Like part 1, but the cats and trees readings are greater
    than the target and pomeranians and goldfish are less than."""
    for n, sue in enumerate(sue_list):
        matches = 0
        for a in sue:
            if a in ['cats','trees']:
                if sue[a] > target_sue[a]:
                    matches += 1
            elif a in ['pomeranians','goldfish']:
                if sue[a] < target_sue[a]:
                    matches += 1
            elif sue[a] == target_sue[a]:
                matches += 1
            if matches == 3:
                print("Sue #", n + 1)

#print(part1())
print(part2())
print("Time (secs):",time.time()-starting_time)