# Advent of Code 2015 Day 15
# https://adventofcode.com/2015/day/15

import time
from random import randint
from itertools import permutations

starting_time = time.time()
testing = False#True
with open('day15.txt') as f:
    lst = list()
    properties = list()
    lines = f.readlines()
    for string in lines:
        string2 = string.split(' ')
        #print(string2)
        properties.append(string2[0])
        lst2 = list()
        for i in [2,4,6,8,10]:
            try:
                lst2.append(int(string2[i][:1]))
                if testing:
                    print("tried.",string2[i][:1])
            except ValueError:
                if testing:
                    print("except",string2[i])
                if string2[i][0] == '-':
                    lst2.append(-int(string2[i][1:2]))
        lst.append(lst2)
    # for x in lst:
    #     if x[0] not in properties:
    #         properties.append(x[0])
print(properties)
print(lst)

def cals():
    """Generates all the combinations of properties that
    will add up to exactly 500 calories"""
    output = list()

    for a in range(1,50):
        for b in range(1,50):
            for c in range(1,50):
                for d in range(1,50):
                    if a + b+ c+d==100 and 5*a + 8*b + 6*c + d == 500:
                        output.append([a,b,c,d])
    return output

def solvePart1():
    """Chooses amounts adding up to 100, multiplies through
    by property, finds product of properties."""

    highest = 0
    best_nums = 0
    for j in range(1000000):
        random_numbers_chosen = False
        while not random_numbers_chosen:
            a,b,c = (randint(1,50),randint(1,50),randint(1,50))
            d = 100 - sum([a,b,c])
            if d > 0:
                random_numbers_chosen = True

    #print([a,b,c,d])
    #multiply the properties by the amounts a,b,c,d
    combined_lst = [a*lst[0][i]+b*lst[1][i]+c*lst[2][i]+d*lst[3][i] for i in range(4)]
    product = 1
    for n in combined_lst:
        if n < 0:
            n = 0
        product *= n
    if product > highest:
        highest = product
        best_nums = [a,b,c,d]
        best_clist = combined_lst
    return highest,best_nums,best_clist

def solvePart2():
    """Solves just like Part 1, but calories have to be 500."""

    highest = 0
    best_nums = 0
    # part 2 uses the combinations that will add up to 500 cals
    cals_lst = cals()
    for vals in cals_lst:
        a,b,c,d = vals[0],vals[1],vals[2],vals[3]
        #multiply the properties by the amounts a,b,c,d
        combined_lst = [a*lst[0][i]+b*lst[1][i]+c*lst[2][i]+d*lst[3][i] for i in range(4)]
        product = 1
        for n in combined_lst:
            if n < 0:
                n = 0
            product *= n
        if product > highest:
            highest = product
            best_nums = [a,b,c,d]
            best_clist = combined_lst
    return highest,best_nums,best_clist


print(solvePart2())
print("Time (secs):",time.time()-starting_time)