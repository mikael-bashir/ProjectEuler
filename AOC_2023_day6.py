from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular

initial = datetime.now()


# part 1

product = 1

time = [34, 90, 89, 86]
distance = [204, 1713, 1210, 1780]
# time = [7, 15, 30]
# distance = [9, 40, 200]

for i in range(len(time)):
    t = time[i]//2
    lower, upper = t, t
    temp = distance[i]
    while (time[i]-lower)*lower > temp:
        lower -= 1
    while (time[i]-upper)*upper > temp:
        upper += 1
    lower += 1
    upper -= 1
    product *= upper - lower + 1

print(product)

# part 2

time = 34908986
distance = 204171312101780
t = time//2
lower, upper = t, t
while (time-lower)*lower > distance:
    lower -= 1
lower += 1
upper = time - lower
ways = upper - lower + 1

print(ways)

runTime = datetime.now() - initial

print()
print(runTime)



