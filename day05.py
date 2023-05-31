# Advent of Code 2015 Day 5
# https://adventofcode.com/2015/day/5

import time

starting_time = time.time()
vowels = 'aeiou'

with open('day05.txt') as f:
    lst = []
    lines = f.readlines()
    #lst = lines[:5]
    #print(lines[:5])

def three_vowels(s):
    """Returns True if s contains at least 3 vowels"""
    vowelnum = 0
    remaining_vowels = 'aeiou'
    for char in s:
        if char in remaining_vowels:
            vowelnum += 1
            remaining_vowels.replace(char,'')
            if vowelnum >= 3:
                return True
    return False

def doubled(s):
    """Returns True if s contains a doubled string"""
    for char in s:
        if char+char in s:
            return True
    return False

def bad_strings(s):
    bads = ['ab', 'cd', 'pq', 'xy']
    for bad in bads:
        if bad in s:
            return True
    return False

def nice(s):
    return three_vowels(s) and doubled(s) and not bad_strings(s)

# nice_strings = 0
# for s in lines:
#     if nice(s):
#         nice_strings += 1

#print("Number of nice strings:",nice_strings)

def two_pair(s):
    """Returns True if s contains a repetition of two letter pair"""
    for i,v in enumerate(s):
        if i < len(s) - 2:
            string = s[i:i+2]
            if string in s[i+2:]:
                return True

    return False

def skip_one(s):
    """Returns True if there's a repeated letter separated by a letter"""
    for i,v in enumerate(s):
        if i < len(s) - 2:
            if s[i+2] == v:
                return True
    return False

def nice2(s):
    return two_pair(s) and skip_one(s)

str2 = 'ieodomkazucvgmuy'
#print(nice2(str2))

nice_strings = 0
for s in lines:
    if nice2(s):
        nice_strings += 1
print("Number of nice strings:",nice_strings)

print("Time (secs):",time.time()-starting_time)
