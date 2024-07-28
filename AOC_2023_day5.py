from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()

# part 1

seeds = []
line1, line2, line3, line4, line5, line6, line7 = False, False, False, False, False, False, False
lines = [line1, line2, line3, line4, line5, line6, line7]
counter = 0

with open('day_5.txt', 'r') as mappings:
    for line in mappings:
        line = line.strip()

        if line == '':
            lines[counter] = True
            if counter > 0:
                lines[counter-1] = False
            counter += 1
            if not lines[0]:
                seeds = temp
                temp = [0 for i in range(len(seeds))]
            continue

        if not (line1 or line2 or line3 or line4 or line5 or line6 or line7):
            line = line[7:len(line)]
            seeds = line.split(' ')
            line1 = True
            for i in range(len(seeds)):
                seeds[i] = int(seeds[i])
            temp = [0 for i in range(len(seeds))]
            continue

        line = line.split(' ')
        line[0], line[1], line[2] = int(line[0]), int(line[1]), int(line[2])
        for i in range(len(seeds)):
            if (line[1] <= seeds[i]) and (seeds[i] <= (line[1]+line[2]-1)):
                temp[i] = seeds[i] - line[1] + line[0]

seeds = temp

print(min(seeds))

runTime = datetime.now() - initial

print()
print(runTime)

# part 2

second = datetime.now()

seeds = []
temp1 = []
line1, line2, line3, line4, line5, line6, line7 = False, False, False, False, False, False, False
lines = [line1, line2, line3, line4, line5, line6, line7]
counter = 0

def setMapper(pair, triplet):
    if ((triplet[1] + triplet[2] - 1) >= (pair[0]) and (triplet[1]) <= (pair[0] + pair[1] - 1)) or \
            ((pair[0] + pair[1] - 1) >= (triplet[1]) and (pair[0] <= (triplet[1] + triplet[2] - 1))):
        const = triplet[0] - triplet[1]
        return [max([triplet[1], pair[0]]) + const, min([(triplet[1] + triplet[2] - 1), pair[0] + pair[1] - 1]) + const]
    else:
        return []

with open('day_5.txt', 'r') as mappings:
    for line in mappings:
        line = line.strip()

        if line == '':
            lines[counter] = True
            if counter > 0:
                lines[counter-1] = False
            counter += 1
            if not lines[0]:
                seeds = temp
                temp = []
            continue

        if not (line1 or line2 or line3 or line4 or line5 or line6 or line7):
            line = line[7:len(line)]
            seeds = line.split(' ')
            line1 = True
            for i in range(len(seeds)):
                seeds[i] = int(seeds[i])
            for i in range(len(seeds)):
                if i%2 == 0:
                    temp1.append([seeds[i], seeds[i+1]])
            seeds = temp1
            temp = []
            continue

        line = line.split(' ')
        line[0], line[1], line[2] = int(line[0]), int(line[1]), int(line[2])
        for i in range(len(seeds)):
            temp1 = setMapper(seeds[i], line)
            if temp1 != []:
                temp1 = [temp1[0], temp1[1] - temp1[0] + 1]
                if not (temp1 in temp):
                    temp.append(temp1)


seeds = temp
temp = []
for i in seeds:
    temp.append(i[0])

print(min(temp))

runTime2 = datetime.now() - second
print(runTime2)





