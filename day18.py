#Advent of Code 2015 Day 18 (Game of Life)
#https://adventofcode.com/2015/day/18

from random import choice

with open('day18.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(lines)
    print(len(lines),len(lines[0]))

GRID_W = 100
GRID_H = 100

teststate = ['##.#.#','...##.','#....#','..#...','#.#..#','####.#']
generation = 0


class Cell:
    def __init__(self, c, r, state=0):
        self.c = c
        self.r = r
        if state == 0:
            self.state = 0
        elif state == 1:
            self.state = 1
        elif state == '.':
            self.state = 0
        else:
            self.state = 1

    # def display(self):
    #     if self.state == 1:
    #         fill(0)  # black
    #     else:
    #         fill(255)  # white
    #     rect(SZ * self.r, SZ * self.c, SZ, SZ)

    def checkNeighbors(self):
        # if self.state == 1: return 1 #on cells stay on
        neighbs = 0  # check the neighbors
        if self.r == 0:
            if self.c == 0:
                for dr, dc in [[1, 0], [0, 1], [1, 1]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1
            elif self.c == GRID_W-1:
                for dr, dc in [[1,0],[0, -1],[1,-1]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1
            else:
                for dr, dc in [[1,0],[0, -1],[0,1],[1,-1],[1,1]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1

        elif self.r == GRID_H-1:
            if self.c == 0:
                for dr, dc in [[-1, 0], [0, 1], [-1, 1]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1
            elif self.c == GRID_W - 1:
                for dr, dc in [[0, -1],[-1,-1],[-1,0]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1
            else:
                for dr, dc in [[-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1]]:
                    if cellList[self.r + dr][self.c + dc].state == 1:
                        neighbs += 1
        elif self.c == 0:
            for dr, dc in [[-1, 0],[1,0],[0,1],[1,1],[-1,1]]:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
        elif self.c == GRID_W-1:
            for dr, dc in [[-1, 0],[1,0],[0,-1],[1,-1],[-1,-1]]:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
        else:
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
        if self.state == 1:
            #print("My state was 1")
            if neighbs in [2, 3]:
                #print("new state 1")
                return 1
            #print("new state 0")
            return 0
        if neighbs == 3:
            #print("new state 1")
            return 1
        #print("New state 0")
        return 0

def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    newList = []  # empty list for cells
    # populate the initial cell list
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList[j].append(Cell(i, j, lines[j][i]))
    #four corners
    newList[0][0].state = 1
    newList[GRID_H-1][0].state = 1
    newList[0][GRID_W-1].state = 1
    newList[GRID_H - 1][GRID_W-1].state = 1
    return newList




def part1():
    global cellList
    cellList = createCellList()
    # for row in cellList:
    #     for c in row:
    #         print(c.state,end='')

    for i in range(100):
        cellList = update(cellList)
        ons = 0
        for row in cellList:
            for col in row:
                #print(col.state,end='')
                if col.state == 1:
                    ons += 1
            #print('')
        #print()
    print("Number of ons:",ons)

def update(cellList):
    newList = []
    for r, row in enumerate(cellList):
        newList.append([])
        for c, cell in enumerate(row):
            newList[r].append(Cell(c, r, cell.checkNeighbors()))
        # four corners
    newList[0][0].state = 1
    newList[GRID_H - 1][0].state = 1
    newList[0][GRID_W - 1].state = 1
    newList[GRID_H - 1][GRID_W - 1].state = 1
    return newList[::]

part1()

