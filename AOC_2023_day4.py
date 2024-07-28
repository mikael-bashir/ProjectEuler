from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()

#part 1

sum = 0


with open("day_4.txt", 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line[10:len(line)]
        line = line.split(" | ")
        winning = line[0].split(' ')
        while '' in winning:
            winning.remove('')
        numbers = line[1].split(' ')
        while '' in numbers:
            numbers.remove('')
        temp = len(set(winning)) + len(set(numbers)) - len(set(winning + numbers))
        if temp > 0:
            sum += 2**(temp-1)

print(sum)


#part 2


arr = []
for i in range(209):
    arr.append(1)

sum = 0
counter = 0


with open("day_4.txt", 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line[10:len(line)]
        line = line.split(" | ")
        winning = line[0].split(' ')
        while '' in winning:
            winning.remove('')
        numbers = line[1].split(' ')
        while '' in numbers:
            numbers.remove('')
        temp = len(set(winning)) + len(set(numbers)) - len(set(winning + numbers))
        if temp > 0:
            for i in range(counter+1, counter+temp+1):
                try:
                    arr[i] += arr[counter]
                except:
                    break
        counter += 1

for i in arr:
    sum += i

print(sum)
runTime = datetime.now() - initial

print()
print(runTime)



