# Advent of Code 2015 Day 12
# https://adventofcode.com/2015/day/12

import time

starting_time = time.time()

digits = '0123456789'
teststr = '[1,"red",5]'

with open('day12.txt') as f:
    lst = f.readlines()
    print(len(lst),lst[:10])

def part1(st,testing=False):
    isnum = False
    nums = list()
    total = 0
    for i,c in enumerate(st):
        if not isnum:
            num = ''
        if testing:
            print("i,c,num:",i,c,num)
        if c not in digits:
            if not isnum:
                continue
            else:
                nums.append(num)
                total += int(num)
                num = ''
                isnum = False
        else:
            isnum = True
            if st[i-1] == '-':
                num += st[i-1]
            num += c
    if testing:
        print(nums)
        print(total)
    return total


def part2(st,testing=False):
    isbracket = False
    blist = list()
    total = 0
    s = ''
    for i, c in enumerate(st):
        if c == '{':
            isbracket = True
            continue
        if isbracket:
            s += c
        if c == '}' and isbracket:
            isbracket = False
            if '"red"' in s:
                blist.append(s)
                total += part1(s,False)
            s = ''
    if testing:
        for i in range(5):
            print(i,blist[i])
    print(total)

#print(part1(lst[0],True)) #119433
print(part2(lst[0],True)) #37714 too low: part1-part2 is too high


print("Time (secs):",time.time()-starting_time)