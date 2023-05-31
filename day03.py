# Advent of Code 2015 Day 3
# https://adventofcode.com/2015/day/3

with open('day03.txt') as f:
    lst = []
    lines = f.readlines()
    lst = lines[0]

locs = set()
santaloc = [0,0]
roboloc = [0,0]
locs.add(tuple(santaloc))
#lst = '^v^v^v^v^v'
for i,val in enumerate(lst):
    if i % 2 == 0:
        if val == '^':
            santaloc[1] -= 1
        elif val == 'v':
            santaloc[1] += 1
        elif val == '<':
            santaloc[0] -= 1
        elif val == '>':
            santaloc[0] += 1
        locs.add(tuple(santaloc))
    else:
        if val == '^':
            roboloc[1] -= 1
        elif val == 'v':
            roboloc[1] += 1
        elif val == '<':
            roboloc[0] -= 1
        elif val == '>':
            roboloc[0] += 1

        locs.add(tuple(roboloc))
#print(lst[:10])
#print(locs)

print(len(locs))

