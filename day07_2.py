# Advent of Code 2015 Day 7
# https://adventofcode.com/2015/day/7
# from https://www.reddit.com/r/adventofcode/comments/3vr4m4/day_7_solutions/

import time

starting_time = time.time()

with open('day07.txt') as f:
    lst = []
    lines = f.readlines()
    for line in lines:
        lst.append(line)#.split(" "))
    #print(lst[:5])

calc = dict()
results = dict()

for command in lst: #divide every line on arrow
    (ops, res) = command.split('->')
    #calc dict is indexed by destination wire
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

print("Part 1 a:",calculate('a')) #956 correct!
print("Time:",time.time()-starting_time)