#!/bin/python3
import random as rng
import sys

def help():
    print("RollDice is a CLI Tool to generate random numbers\n")
    print("-s Silence (Only display the generated numbers)")
    print("-m Max number (Dice sides) DEFAULT: 6")
    print("-n Min number DEFAULT: 1")
    print("-t Number of rolls to make")
    print("-h Show this help and quit")
    exit(0)


args = sys.argv[1:]
#-s silence
sFlag = 0
#-m max
mFlag = 6
#-n min
nFlag = 1
#-t times
tFlag = 1
i=0
rolls=[]
for arg in args:
    if arg=="-s":
        sFlag=1
    if arg=="-m":
        mFlag=int(args[i+1])
    if arg=="-n":
        nFlag=int(args[i+1])
    if arg=="-t":
        tFlag=int(args[i+1])
    if arg=="-h":
        help()
    i+=1

for j in range(0,tFlag):
    rolls.append(rng.randint(nFlag,mFlag))

Pretext = "Dice #"
if sFlag==0:
    for k in range(0,tFlag):
        whatprint = Pretext + str(k+1) + ": " + str(rolls[k])
        print(whatprint)
else:
    for k in range(0,tFlag):
        print(rolls[k])



