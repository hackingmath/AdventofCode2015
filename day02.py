# Advent of Code 2015 Day 2
# https://adventofcode.com/2015/day/2

with open('day02.txt') as f:
    lst = []
    lines = f.readlines()
    for line in lines:

        lst1 = [int(x) for x in line.split('x')]
        lst1.sort()
        lst.append(lst1)
print(lst[:5])
total = 0
bow = 0
for box in lst:
    total += 3*box[1]*box[0] + 2*box[1]*box[2] + 2*box[2]*box[0]
    bow += 2*(box[0]+box[1]) + box[0]*box[1]*box[2]
print("total:",total)
print("bow:",bow)

