# Advent of Code 2015 Day 1
# https://adventofcode.com/2015/day/1

with open('day01.txt') as f:
    #lst = []
    lines = f.readlines()
    lst = lines[0]
print(len(lst))
start = 0
for char in lst:
    if char == '(':
        start += 1
    else:
        start -= 1
print("end:",start)

start = 0
for position,char in enumerate(lst):
    if char == '(':
        start += 1
    else:
        start -= 1
    if start == -1:
        print("basement on position ",position + 1)

