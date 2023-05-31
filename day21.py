# Advent of Code 2015 Day 21
# https://adventofcode.com/2015/day/21

import time
from random import sample,choice
from itertools import combinations

starting_time = time.time()

#cost,damage,armor
weapons = [[8,4,0],
           [10,5,0],
           [25,6,0],
           [40,7,0],
           [74,8,0]]

armor = [[13,0,1],
         [31,0,2],
         [53,0,3],
         [75,0,4],
         [102,0,5]]

rings = [[25,1,0],
         [50,2,0],
         [100,3,0],
         [20,0,1],
         [40,0,2],
         [80,0,3]]

boss = [104,8,1] #hit points, damage, armor

def total(items):
    """Adds cost, damage, armor of
    array of lists"""
    output = [0,0,0]
    for l in items:
        output[0] += l[0]
        output[1] += l[1]
        output[2] += l[2]
    return output

def choose_items():
    """One weapon, 0-1 armor and 0-2 rings"""
    output = list()
    weap = choice(weapons)
    arm = sample(armor,choice([0,1]))
    ring = sample(rings,choice([0,1,2]))
    output = [weap]
    if len(arm) == 1:
        output.append(arm[0])
    if len(ring) >= 1:
        output.append(ring[0])
    if len(ring) == 2:
        output.append(ring[1])

    return output

def play(me,bos,testing=False):
    """Simulates play between me and boss
    until one's hit points = 0"""
    my = [100,me[0],me[1]]
    b = bos[::]
    my_damage = my[1] - b[2]
    if testing:
        print("my damage:",my_damage)
    boss_damage = b[1] - my[2]
    while True:
        b[0] -= my_damage
        if testing:
            print("boss:",b[0])
        if b[0] <= 0:
            return 1
        my[0] -= boss_damage
        if testing:
            print("me:",my[0])
        if my[0] <= 0:
            return 0

def part1():
    lowest = 1000
    gear = []
    for i in range(10000):
        stuff = choose_items()
        tot = total(stuff)
        #print(tot)
        cost = tot[0]
        outcome = play([tot[1],tot[2]],boss)
        #print("outcome:",outcome)
        if (outcome == 1) and (cost < lowest):
            lowest = cost
            gear = stuff
            besttotal = total(gear)
    print("lowest:",lowest)
    print("gear:",gear)
    print("best total",besttotal)

def part2():
    highest = 0
    gear = []
    for i in range(10000):
        stuff = choose_items()
        tot = total(stuff)
        # print(tot)
        cost = tot[0]
        outcome = play([tot[1], tot[2]], boss)
        # print("outcome:",outcome)
        if (outcome == 0) and (cost > highest):
            highest = cost
            gear = stuff
            besttotal = total(gear)
    print("highest:", highest)
    print("gear:", gear)
    print("best total", besttotal)

#print(play([7,0],boss,True))
#part1()
part2()
print("Time (secs):",time.time()-starting_time)