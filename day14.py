# Advent of Code 2015 Day 14
# https://adventofcode.com/2015/day/14

import time
from itertools import permutations

starting_time = time.time()

with open('day14.txt') as f:
    lst = list()
    names = list()
    lines = f.readlines()
    for string in lines:
        #one_line = list()
        string2 = string.split(' ')
        lst.append([string2[0],int(string2[3]),int(string2[6]),int(string2[13]),])

    for x in lst:
        if x[0] not in names:
            names.append(x[0])

def distance(arr,num_secs):
    """Calculates the distance traveled by the reindeer
    in the array in the given number of seconds."""
    speed,duration,rest = arr[1:]
    #print("check!")
    t = 0
    dist = 0
    while t < num_secs:
        if num_secs >= t + duration:
            dist += speed*duration
            t += duration + rest
            #print("if done.")
        else:
            time_left = num_secs - t
            dist += speed * time_left
            t += time_left
            #print("else done.")
    #print(arr[0],dist)
    return dist


def solvePart1():
    """Puts the reindeer's distance traveled in the distances
    list and returns the maximum distance"""
    return max([distance(reindeer,2503) for reindeer in lst])

def solve():
    """Loops through each second, giving the reindeer with
     the max distance a point."""
    points = [0]*len(names)
    for i in range(1,2504):
        distances = [distance(reindeer,i) for reindeer in lst]
        idx = distances.index(max(distances))
        points[idx] += 1

    return max(points)


#print(lines[:10])
print(lst[:10])

print(names)
#print(distance(["Comet",14,10,127],1000))
print(solve())
print("Time (secs):",time.time()-starting_time)