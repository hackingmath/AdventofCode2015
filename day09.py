# Advent of Code 2015 Day 9
# https://adventofcode.com/2015/day/9

import time
from itertools import permutations

starting_time = time.time()

with open('day09.txt') as f:
    lst = list()
    cities = list()
    for line in f.readlines():#:
        words = line.split(' ')
        lst.append([words[0],words[2],int(words[4])])
        if words[0] not in cities:
            cities.append(words[0])
        if words[2] not in cities:
            cities.append(words[2])
print(lst)

#testlst = [['London','Dublin',464],['London','Belfast',518],['Belfast','Dublin',141],]
print(cities)
#testcities = ['London',"Dublin","Belfast"]
def distance(A,B,distlst=lst):
    for route in distlst:
        if A in route and B in route:
            return route[2]

def routelength(arr,citylist=cities):
    total = 0
    for i,v in enumerate(arr):
        if i < len(arr)-1:
            total += distance(citylist[v],citylist[arr[i+1]])
    return total



distances = [routelength(route) for route in permutations(list(range(len(cities))),len(cities))]
#distances = [routelength(route,testcities) for route in permutations(list(range(3)),3)]
print(distances)
print("lowest:",max(distances))

#print(distance("Faerun",'Norrath'),distance("Tambi","AlphaCentauri"))


print("Time (secs):",time.time()-starting_time)