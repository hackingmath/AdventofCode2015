# Advent of Code 2015 Day 20
# https://adventofcode.com/2015/day/20

import time
from math import sqrt
#from random import randint
from itertools import combinations

starting_time = time.time()

def factor(n):
    '''Calculates all factors of n,
    multiplies each by 10 then sums
    them up'''
    factors = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            factors.add(10*i)
            factors.add(10*(n/i))
    return sum(factors)

def factor2(n):
    '''Calculates all factors of n,
    deletes all less than n/50,
    multiplies each by 11 then sums
    them up'''
    factors = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            if i > n/50:
                factors.add(11*i)
            if (n/i > n/50):
                factors.add(11*(n/i))
    return sum(factors)

def part1():

    house = 500000
    while True:
        if factor(house) > 36000000:
            print(house, factor(house))
            break
        if house % 10000 == 0:
            print("house:",house)
        house += 1

def part2():
    # house_dict = {i:0 for i in range(1,10000000)}
    # for elf in range(1,1000000):
    #     multiple = 1
    #     while multiple < 51:
    #         try:
    #             house_dict[elf*multiple] += 11*elf
    #             if house_dict[elf * multiple] >= 36000000:
    #                 return elf * multiple
    #             multiple+=1
    #         except KeyError:
    #             continue

    house = 700000
    while True:
        if factor2(house) > 36000000:
            print(house, factor2(house))
            break
        if house % 10000 == 0:
            print("house:",house)
        house += 1



#print(factor(500),factor(1000),factor(900000))
#500: 10920, 1000: 23400, 900000: 31990140
#but starting at house 900,000 was too high:
#900900 37914240
#part1()

#print(factor2(1200000))
print(part2())
print("Time (secs):",time.time()-starting_time)