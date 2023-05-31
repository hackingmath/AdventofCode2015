# Advent of Code 2015 Day 7
# https://adventofcode.com/2015/day/7

import time

starting_time = time.time()


with open('day07.txt') as f:
    lst = []
    lines = f.readlines()
    for line in lines:
        lst.append(line.split(" "))
    #print(lst[:5])

vals = dict()

def instr(msg):
    """Performs instruction given by message"""
    if msg[1] == '->':
        dest = msg[-1][:-1]
        print("dest:",dest)
        if dest not in vals:
            try:
                intval = int(msg[0])
                vals[dest] = intval
            except ValueError:
                print(vals)
                vals[dest] = vals[msg[0]]
        else:
            try:
                intval = int(msg[0])
                vals[dest] += intval
            except ValueError:
                vals[dest] += vals[msg[0]]
    elif msg[1] == 'AND':
        if msg[0] not in vals:
            vals[msg[0]] = 0
        if msg[2] not in vals:
            vals[msg[2]] = 0
        dest = msg[-1][:-1]
        print("dest",dest)
        if dest not in vals:

            vals[dest] = vals[msg[0]] & vals[msg[2]]
        else:
            vals[dest] += vals[msg[0]] & vals[msg[2]]

    elif msg[1] == 'OR':
        if msg[0] not in vals:
            vals[msg[0]] = 0
        if msg[2] not in vals:
            vals[msg[2]] = 0
        dest = msg[-1][:-1]
        if dest not in vals:
            vals[dest] = vals[msg[0]] | vals[msg[2]]
        else:
            vals[dest] += vals[msg[0]] | vals[msg[2]]

    elif msg[1] == 'LSHIFT':
        if msg[0] not in vals:
            vals[msg[0]] = 0
        if msg[2] not in vals:
            vals[msg[2]] = 0
        dest = msg[-1][:-1]
        if dest not in vals:
            vals[dest] = vals[msg[0]] << int(msg[2])
        else:
            vals[dest] += vals[msg[0]] << int(msg[2])

    elif msg[1] == 'RSHIFT':
        if msg[0] not in vals:
            vals[msg[0]] = 0
        if msg[2] not in vals:
            vals[msg[2]] = 0
        dest = msg[-1][:-1]
        if dest not in vals:
            vals[dest] = vals[msg[0]] >> int(msg[2])
        else:
            vals[dest] += vals[msg[0]] >> int(msg[2])

    else: #NOT
        if msg[1] not in vals:
            vals[msg[1]] = 0
        dest = msg[-1][:2]
        if dest not in vals:
            vals[dest] = 65535-vals[msg[1]]#~vals[msg[1]]
        else:
            vals[dest]  += 65535-vals[msg[1]]#~vals[msg[1]]

for inst in lst:
    try:
        instr(inst)
    except TypeError:
        print("inst:",inst)

print(vals)
print("a",vals['a'])
print("lx",vals['lx'])
print("lw",vals['lw'])
print("lv",vals['lv'])
print("lc",vals['lc'])

print("Time (secs):",time.time()-starting_time)
