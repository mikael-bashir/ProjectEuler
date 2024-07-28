from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()

#part 1

def numSub(lines):
    results = []
    startP = -1
    endP = -1
    for i in range(0, len(lines)):
        try:
            if startP == -1:
                test = int(lines[i])
                startP = i
        except:
            continue
        try:
            if startP != -1:
                test = int(lines[i])
        except:
            endP = i-1
        if (startP != -1) and (i == len(lines)-1) and (endP == -1):
            endP = i
        if (startP != -1) and (endP != -1):
            results.append([startP, endP])
            startP = -1
            endP = -1
    return results

arr = []
with open("day_3.txt", 'r') as scheme:
    for line in scheme:
        line = line.strip()
        arr.append(line)

sum = 0
for i in range(len(arr)):
    temp = numSub(arr[i])
    for j in temp:
        isNum = False
        if i>0:
            for k in range(j[0], j[1]+1):
                if (not isinstance(arr[i-1][k], int)) and (arr[i-1][k] != '.'):
                    isNum = True
                    break
        if isNum:
            sum += int(arr[i][j[0]: j[1]+1])
            #print(int(arr[i][j[0]: j[1] + 1]))
            continue
        if i<(len(arr)-1):
            for k in range(j[0], j[1]+1):
                if (not isinstance(arr[i+1][k], int)) and (arr[i+1][k] != '.'):
                    isNum = True
                    break
        if isNum:
            sum += int(arr[i][j[0]: j[1]+1])
            #print(int(arr[i][j[0]: j[1] + 1]))
            continue
        if 0<j[0]:
            if (not isinstance(arr[i][j[0]-1], int)) and (arr[i][j[0]-1] != '.'):
                isNum = True
        if isNum:
            sum += int(arr[i][j[0]: j[1]+1])
            #print(int(arr[i][j[0]: j[1]+1]))
            continue
        if j[1]<(len(arr[0])-1):
            if (not isinstance(arr[i][j[1]+1], int)) and (arr[i][j[1]+1] != '.'):
                isNum = True
        if isNum:
            sum += int(arr[i][j[0]: j[1]+1])
            #print(int(arr[i][j[0]: j[1] + 1]))
            continue
        if 0<j[0] and 0<i:
            if (not isinstance(arr[i-1][j[0]-1], int)) and (arr[i-1][j[0]-1] != '.'):
                isNum = True
        if 0<j[0] and i<(len(arr)-1):
            if (not isinstance(arr[i+1][j[0]-1], int)) and (arr[i+1][j[0]-1] != '.'):
                isNum = True
        if j[1]<(len(arr[0])-1) and 0<i:
            if (not isinstance(arr[i-1][j[1]+1], int)) and (arr[i-1][j[1]+1] != '.'):
                isNum = True
        if j[1]<(len(arr[0])-1) and i<(len(arr)-1):
            if (not isinstance(arr[i+1][j[1]+1], int)) and (arr[i+1][j[1]+1] != '.'):
                isNum = True
        if isNum:
            sum += int(arr[i][j[0]: j[1]+1])
            #print(int(arr[i][j[0]: j[1] + 1]))


#print("#-------------")
print(sum)
print()

#part 2

coordinates=[]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == '*':
            coordinates.append([i, j])

sum = 0
for i in coordinates:
    temp1, temp2, temp3 = -1, -1, -1
    number = 0
    current = -1
    temp1 = numSub(arr[i[0]])
    if i[0]>0:
        temp2 = numSub(arr[i[0]-1])
    if i[0]<(len(arr)-1):
        temp3 = numSub(arr[i[0]+1])
    for j in temp1:
        if (j[0]-1) <= i[1] and i[1] <= (j[1]+1):
            if current == -1:
                current = int(arr[i[0]][j[0]: j[1]+1])
            else:
                current *= int(arr[i[0]][j[0]: j[1]+1])
            number += 1
    if temp2 != -1:
        for j in temp2:
            if (j[0]-1) <= i[1] and i[1] <= (j[1]+1):
                if current == -1:
                    current = int(arr[i[0]-1][j[0]: j[1] + 1])
                else:
                    current *= int(arr[i[0]-1][j[0]: j[1] + 1])
                number += 1
    if temp3 != -1:
        for j in temp3:
            if (j[0]-1) <= i[1] and i[1] <= (j[1]+1):
                if current == -1:
                    current = int(arr[i[0]+1][j[0]: j[1] + 1])
                else:
                    current *= int(arr[i[0]+1][j[0]: j[1] + 1])
                number += 1
    if number == 2:
        sum += current

print()
print(sum)


runTime = datetime.now() - initial

print()
print(runTime)



