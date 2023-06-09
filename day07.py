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

calc = dict()
vals = dict()

for command in lst:
    (ops,res) = command.split("->")
    # calc dict is indexed by destination wire
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    """Performs instruction given by message"""
    try:
        return int(name)
    except ValueError:
        pass

    # if msg[1] == '->':
    #     dest = msg[-1][:-1]
    #     print("dest:",dest)
    #     if dest not in vals:
    #         try:
    #             intval = int(msg[0])
    #             vals[dest] = intval
    #         except ValueError:
    #             print(vals)
    #             vals[dest] = vals[msg[0]]
    #     else:
    #         try:
    #             intval = int(msg[0])
    #             vals[dest] += intval
    #         except ValueError:
    #             vals[dest] += vals[msg[0]]
    if name not in vals:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
                res = calculate(ops[0]) | calculate(ops[2])
            elif op == "LSHIFT":
                res = calculate(ops[0]) << calculate(ops[2])
            elif op == "RSHIFT":
                res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'NOT':
                res = ~calculate(ops[1]) & 0xffff
        vals[name] = res
    return vals[name]

print(vals)
print("a",vals['a'])
print("lx",vals['lx'])
print("lw",vals['lw'])
print("lv",vals['lv'])
print("lc",vals['lc'])

print("Time (secs):",time.time()-starting_time)
