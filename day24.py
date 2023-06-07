# Advent of Code 2015 Day 24
# https://adventofcode.com/2015/day/24
# help from Reddit: semi225599 https://www.reddit.com/r/adventofcode/comments/3y1s7f/day_24_solutions/

import time
from random import randint,choice
from itertools import combinations
from functools import reduce
from operator import mul

starting_time = time.time()

with open('day24.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [int(x.strip("\n")) for x in lines]
    print(len(lines), sum(lines),sum(lines)/3,lines)

def trisect(arr,testing=False):
    total = sum(arr)/3
    out1,out2,out3 = list(),list(),list()
    outlists = [out1,out2,out3]
    if testing:
        print("total:",total)


testarr = [1,2,3,4,5,7,8,9,10,11]
def part1(testing=False):
    print(trisect(testarr,testing))


def part2(testing=False):
    pass

def day_24(arr,num_groups,testing=False):
    """semi225599's concise solution"""
    group_sz = sum(arr) // num_groups
    for i in range(len(arr)):
        qes = [reduce(mul,c) for c in combinations(arr,i) if sum(c) == group_sz]
        if qes:
            if testing:
                print(qes)
            return min(qes)

#part1(True)
#print(part2())

print(day_24(lines,4,True))
print("Time (secs):",time.time()-starting_time)