from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()


#PART 1

red = 12
green = 13
blue = 14
counter = 1
sum = 0

with open("day_2.txt", 'r') as games:
    for line in games:
        isPossible = True
        line.strip()
        temp = line.split(' ', 2)
        temp = temp[2:len(temp)]
        line = temp[0]
        line = line.replace(';', ',')
        line = line.split(', ')
        for i in line:
            if i.split(' ')[1] == "red":
                if int(i.split(' ')[0]) > red:
                    isPossible = False
            if i.split(' ')[1] == "blue":
                if int(i.split(' ')[0]) > blue:
                    isPossible = False
            if i.split(' ')[1] == "green":
                if int(i.split(' ')[0]) > green:
                    isPossible = False
        if isPossible:
            sum += counter
        counter += 1

print(sum)

#PART 2


sum = 0
counter = 1

with open("day_2.txt", 'r') as games:
    for line in games:
        red = []
        green = []
        blue = []
        line = line.strip()
        temp = line.split(' ', 2)
        temp = temp[2:len(temp)]
        line = temp[0]
        line = line.replace(';', ',')
        line = line.split(', ')
        for i in line:
            if i.split(' ')[1] == "red":
                red.append(int(i.split(' ')[0]))
            if i.split(' ')[1] == "blue":
                blue.append(int(i.split(' ')[0]))
            if i.split(' ')[1] == "green":
                green.append(int(i.split(' ')[0]))
        temp = max(red) * max(blue) * max(green)
        sum += temp
        counter += 1


print(sum)

runTime = datetime.now() - initial

print()
print(runTime)



