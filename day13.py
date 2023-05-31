# Advent of Code 2015 Day 13
# https://adventofcode.com/2015/day/13

import time
from itertools import permutations

starting_time = time.time()

with open('day13.txt') as f:
    lst = list()
    names = ['Peter'] #for part 2. For part 1: list()
    lines = f.readlines()
    for string in lines:
        #one_line = list()
        string2 = string.split(' ')
        lst.append([string2[0],string2[2],int(string2[3]),string2[10].strip(".\n")])

    for x in lst:
        if x[0] not in names:
            names.append(x[0])
        if x[-1] not in names:
            names.append(x[-1])

def cost(A,B):
    """Calculates the gain or cost of sitting
    A and B together"""
    output = 0
    if A == "Peter" or B == "Peter":
        return 0
    for pair in lst:
        if A in pair and B in pair:
            if pair[1] == 'gain':
                output += pair[2]
            else:
                output -= pair[2]
    return output

def solve():

    scores = list()
    length = len(names)
    arrangements = permutations(names,length)
    for i in arrangements:
        output = 0
        for j,name in enumerate(i):
            output += cost(name,i[j-1])
        scores.append(output)
    #print(scores)
    return max(scores)

#print(lines[:10])
#print(lst[:10])
#print(cost('Alice','Bob'),cost("Carol","Bob"))
#print(names)
print(solve())
print("Time (secs):",time.time()-starting_time)