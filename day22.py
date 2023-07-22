# Advent of Code 2015 Day 22
# https://adventofcode.com/2015/day/22

import time
from random import randint,choice
from itertools import combinations

starting_time = time.time()

#my puzzle input: (the boss's hit points and damage)
hit_points = 51
damage = 9

def play(phit,mana,bhit,bdamage,testing=False):
    """Simulates game loop"""
    shield_t,poison_t,recharge_t = 0,0,0
    spells = 'mdspr' #spells to choose from
    costs = {'m':53,'d':73,'s':113,'p':173,'r':229}
    mana_cost = 0
    while True:
        damage = 0
        #sp = choice(spells)
        sp = None
        if mana == 53:
            sp = 'm'
        elif mana > 53:
            sp = choice(spells)
            while costs[sp] > mana:
                sp = choice(spells)
        else: pass
        if testing:
            print('sp,mana:',sp,mana)
        if sp == 'm': #magic missile
            mana -= costs['m']
            mana_cost += 53
            damage = 4
        elif sp == 'd': #drain
            mana -= 73
            mana_cost += 73
            damage += 2
        elif sp == 's': #shield
            mana -= 113
            mana_cost += 113
            damage += 0
            armor = 7
            shield_t = 6
        elif sp == 'p': #poison
            mana -= 173
            mana_cost += 173
            #damage += 3
            poison_t = 6
        elif sp == 'r': #recharge
            mana -= 229
            mana_cost += 229
            #damage = 0
            recharge_t = 5
        else: pass
        if shield_t == 0:
            armor = 0
        if shield_t > 0:
            damage += 3
            shield_t -= 1
        if poison_t > 0:
            damage += 3
            poison_t -= 1
        if recharge_t > 0:
            mana += 101
            recharge_t -= 1
        bhit -= damage
        if testing:
            print("bhit:",bhit)
        #boss's turn
        if bhit <= 0:
            win = True
            return win, mana_cost
        phit -= bdamage
        if phit <= 0:
            return False, mana_cost

def part1(testing=False):
    win = False
    #while win == False:
    while True:
        win, mana = play(50, 500, 51, 9)
        if win and mana > 618:
            print("win,mana:",win,mana)

def part2(testing=False):
    pass

print(part1()) #618 too low
#print(part2())
print("Time (secs):",time.time()-starting_time)