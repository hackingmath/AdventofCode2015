# Advent of Code 2015 Day 19
# https://adventofcode.com/2015/day/19
# with help from "atrocia6" on Reddit
# https://www.reddit.com/r/adventofcode/comments/13lfxxq/2015_day_19_part_1_2_python_deterministic_solution/

import time

starting_time = time.time()

replacements = []
new_molecules = set()
molecules = list()
with open("day19.txt") as f:
    for line in f:
        if line == "\n":
            break
        words = line.split()
        replacements.append((words[0], words[2]))

    molecule = f.readline().strip()
    molecules.append(molecule)
    print("mols:",molecules)
    print("reps:", replacements)

def part1(testing = False):
    for replacement in replacements:
        for m in molecules:
            if testing:
                print("m:",m)
            for i in range(len(m)):
                for j in range(len(replacement[0])):
                    if (i + j == len(m)) or (not m[i + j] == replacement[0][j]):
                        break
                else:
                    new_molecules.add(m[:i] + replacement[1] + m[i + len(replacement[0]):])
    print(len(new_molecules)) #518

part1(True) #518
#print(part2())
print("Time (secs):",time.time()-starting_time)