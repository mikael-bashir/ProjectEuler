from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()

# PART 1

sum = 0

with open("day_1.txt", 'r') as day1:
    for line in day1:
        temp = ""
        line.strip()
        for i in line:
            try:
                if isinstance(int(i), int):
                    temp += i
            except ValueError:
                pass
        temp = temp[0] + temp[-1]
        sum += int(temp)

#print(sum)
#55607

# PART 2

strToNum = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

revToNum = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8,
            'enin': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

sum = 0
all = list(strToNum)
allRev = list(revToNum)
counter = 1

mini, first = 0, "one"

with open("day_1.txt", 'r') as day1:
    for line in day1:
        temp = ""
        line.strip()
        mini = len(line)
        for i in all:
            t = line.find(i)
            if (mini > t) and (t != -1):
                mini = t
                first = i
        temp += str(strToNum.get(first))
        revLine = line[::-1]
        mini = len(line)
        for i in allRev:
            t = revLine.find(i)
            if (mini > t) and (t != -1):
                mini = t
                first = i
        temp += str(revToNum.get(first))
        sum += int(temp)
        counter += 1





print(sum)
#54236

runTime = datetime.now() - initial

print()
print(runTime)



