# Advent of Code 2015 Day 7
# https://adventofcode.com/2015/day/7

import time

starting_time = time.time()

with open('day07.txt') as f:
    lst = []
    lines = f.readlines()
    for line in lines:
        lst.append(line)
    #print(lst[:5])

calc = dict()
vals = dict()

for command in lst:
    (ops,res) = command.split("->")
    #print("ops,res:",ops,res)
    if res.strip() in ['lf','lq','kh','ls','kz']:
        print(command)
    # calc dict is indexed by destination wire
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    """Performs instruction given by message"""
    try:
        return int(name)
    except ValueError:
        pass

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

print("Solution a:",calculate('a')) #956 correct!

print("vals:",vals)
print('calc:',calc['a'])
print("a",vals['a'])
print("b",vals['b'])
print("lw",vals['lw'])
print("lv",vals['lv'])
print("lc",vals['lc'])

print("Time (secs):",time.time()-starting_time)
