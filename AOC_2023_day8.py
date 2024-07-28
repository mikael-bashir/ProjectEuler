from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular
from collections import Counter

initial = datetime.now()

# part 1

'''
instructions = 'LR'
max = len(instructions)-1
nodes = {}
seen = ['AAA']

with open('day_8.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        line = line.split(' = ')
        temp1 = line[1].split(' ')
        nodes.update({line[0]: [temp1[0], temp1[1]]})

node = 'AAA'
print(len(nodes))
current = 0
counter = 0

print(nodes)

while node != 'ZZZ':
    if current > max:
        current = 0
    t = instructions[current]
    if t == 'L':
        node = nodes.get(node)[0]
        #if [node, t] not in seen:
            #seen.append([node, t])
    if t == 'R':
        node = nodes.get(node)[1]
        #if [node, t] not in seen:
            #seen.append([node, t])
    counter += 1
    current += 1

print(counter)

'''

# part 2

instructions = 'LRRLRLRRLRRRLRLRLRRLRRRLRRRLRRLRRRLRLRLRLRLRLRLRRRLRRLRRRLLLLRRRLRLLLRRRLLRLLRRRLRRRLRLRRLRRRLRRRLLRRRLRLRRRLLRRRLRLLRRRLRRLLRLRLRLRRRLRLLRLRLRRRLRLLRLRLRRRLLRRRLRRLRRRLRLRRLRLRRLRLRRLRRRLLRRRLLLRRRLLRRLRRLRRLRLLRRLRRRLRRLRLRLRRLRRLLLRRLRLRRRLRRRLRRRLLLRLRRRLLRRRLRLLRRRR'
max = len(instructions)-1
nodes = {}
window = []
#seen = ['AAA']

with open('day_8.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        line = line.split(' = ')
        temp1 = line[1].split(' ')
        nodes.update({line[0]: [temp1[0], temp1[1]]})

node = []
for i in nodes:
    if i[-1] == 'A':
        node.append(i)

print(node)


current = 0
counter = 0
cycle = []
residue = []

for i in node:
    current = 0
    counter = 0
    test = i
    if current > max:
        current = 0
    t = instructions[current]
    if t == 'R':
        test = nodes.get(i)[1]
    if t == 'L':
        test = nodes.get(i)[0]
    current += 1
    counter += 1
    while test != i:
        current += 1
        counter += 1
        if current > max:
            current = 0
        t = instructions[current]
        if t == 'R':
            test = nodes.get(i)[1]
        if t == 'L':
            test = nodes.get(i)[0]
    cycle.append(counter)
    print(counter)


current = 0
counter = 0
#'''
for j in range(len(node)):
    current = 0
    counter = 0
    while node[j][-1] != 'Z':
        if current > max:
            current = 0
        t = instructions[current]
        print(node, t)
        if t == 'L':
            for i in range(len(node)):
                node[i] = nodes.get(node[i])[0]
            #if [node, t] not in seen:
                #seen.append([node, t])
        if t == 'R':
            for i in range(len(node)):
                node[i] = nodes.get(node[i])[1]
            #if [node, t] not in seen:
                #seen.append([node, t])
        counter += 1
        current += 1
    residue.append(counter)
#'''
print(node)
print(cycle)
print(residue)

runTime = datetime.now() - initial

print()
print(runTime)



