# Advent of Code 2015 Day 19
# https://adventofcode.com/2015/day/19

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
testing = True
reps = list()
starting_str = list()
with open('day19.txt') as f:
    for line in f:
        if line == '\n':
            break
        words = line.split()
        reps.append((words[0],words[2]))
        # #print(lines)
        # for s in lines[:-2]:
        #     s2 = s.split(' => ')
        #     #print(s2)
        #     reps[s2[0]] = s2[1][:-1]
        # starting_str = lines[-1]
    molecules = f.readline().strip()
    starting_str.append(molecules)
    print("reps:",reps)
    print("starting_str:",starting_str)

def replace(str1,str2,place):
    """Replacement of str1 into str2"""
    pass

def part1(testing = False):
    output = set()
    repnum = 0
    for x in reps:
        for s in starting_str:
            if testing:
                print("s:", s)
            for i in range(len(s)):
                for j in range(len(x[0])):

                    if ((i+j) == len(s)) or (not s[i + j] == x[0][j]):
                        break
                else:
                    output.add(s[:i]+x[1]+s[(i+len(x[0])):])
    print("Part 1:",len(output))

def part2():
    pass

part1(True) #281 too low #641 too high 518 correct!
#print(part2())
print("Time (secs):",time.time()-starting_time)