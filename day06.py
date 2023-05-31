# Advent of Code 2015 Day 6
# https://adventofcode.com/2015/day/6

import time

starting_time = time.time()


with open('day06.txt') as f:
    lst = []
    lines = f.readlines()
    for line in lines:
        lst.append(line.split(" "))
    print(lst[:5])

grid = [[0]*1000 for i in range(1000)]

def instr(msg):
    """Performs instruction given by message"""
    if msg[0] == 'toggle':
        start = msg[1].split(",")
        end = msg[3].split(",")
        end[1]=end[1][:-1]
        for r in range(int(start[0]),int(end[0])+1):
            for c in range(int(start[1]),int(end[1])+1):
                # if grid[r][c] == 'on':
                #     grid[r][c] = 'off'
                # else:
                #     grid[r][c] = 'on'
                grid[r][c] += 2
    elif msg[1] == 'on':
        start = msg[2].split(",")
        end = msg[4].split(",")
        end[1] = end[1][:-1]
        for r in range(int(start[0]),int(end[0])+1):
            for c in range(int(start[1]),int(end[1])+1):
                grid[r][c] += 1#grid[r][c] = 'on'
    else: #"off"
        start = msg[2].split(",")
        end = msg[4].split(",")
        end[1] = end[1][:-1]
        for r in range(int(start[0]),int(end[0])+1):
            for c in range(int(start[1]),int(end[1])+1):
                grid[r][c] -= 1 #= 'off'
                if grid[r][c] < 0:
                    grid[r][c] = 0
    #print(start,end)

test = ['turn', 'on', '499,499', 'through', '500,500\n']
for instruction in lst:
    instr(instruction)

ons = 0

for i in range(1000):
    for j in range(1000):
        #if grid[i][j] == 'on':
        ons += grid[i][j]

print("Ons:",ons)

print("Time (secs):",time.time()-starting_time)
