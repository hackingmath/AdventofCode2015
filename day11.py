# Advent of Code 2020 Day 11
# https://adventofcode.com/2015/day/11

import time

starting_time = time.time()

N = 5

alpha = "abcdefghijklmnopqrstuvwxyz"
def required(string,testing=False):
    """Returns True if string passes
    requirements for password
    At least 3 letters in a row
    No i, o or l
    At least 2 different pairs"""
    if testing:
        print("testing",string)
    for letter in 'iol':
        if letter in string:
            if testing:
                print("contains",letter)
            return False
    contains_run = False
    for i,c in enumerate(string):
        idx = alpha.index(c)
        try:
            if string[i+1] == alpha[idx+1] and string[i+2] == alpha[idx + 2]:
                contains_run = True
        except IndexError:
            pass
    if contains_run == False:
        if testing:
            print("no run")
        return False
    repeats = set()
    for i,letter in enumerate(string):
        if i < len(string)-1:
            if string[i+1] == letter:
                repeats.add(letter)
    if testing:
        print(string,"repeats:",repeats)
    if len(repeats) < 2:
        if testing:
            print("too few repeats")
        return False
    return True

def preincrement(string):
    replacements = {'i':'j','o':'p','l':'m'}
    newstring = string[::]
    for i,letter in enumerate(string):
        if letter in replacements:
            newstring = string[:i]+replacements[letter]+(7-i+1)*'a'
            return newstring
    return newstring

def increment(string,place):
    if place > 0:
        letter=string[place]
        if letter == 'z':
            return increment(string[:place],place-1) + 'a'
        else:
            return string[:place]+ alpha[alpha.index(letter) + 1]

testwords = ["hijklmzz","abbceffg","abbcegjk","abcdefgh","abcdffaa",'ghijklmn','ghjaabcc']
for t in testwords:
    print(t,preincrement(t))

pinput = 'vzbxkghb'
pinput2 = 'vzbxxyzz'
testinput1 = 'vzbxkghb' #'abcdffaa'
testinput2 = 'ghijklmn' #'ghjaabcc'

pinput3 = increment(pinput2,7)
while not required(pinput3):
    pinput3 = preincrement(pinput3)
    pinput3 = increment(pinput3,7)

print(preincrement(pinput3))
print("Time (secs):",time.time()-starting_time)