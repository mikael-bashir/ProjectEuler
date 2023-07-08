from datetime import datetime
from math import sqrt
from sympy import primerange

start = datetime.now()


def driver(limit):
    sumDict = {}
    aUpper = int(sqrt(limit))
    bUpper = int(limit ** (1/3))
    cUpper = int(limit ** (1/4))
    for a in primerange(1, aUpper + 1):
        for b in primerange(1, bUpper + 1):
            for c in primerange(1, cUpper + 1):
                summ = a ** 2 + b ** 3 + c ** 4
                if summ <= limit:
                    sumDict[summ] = 1
                else:
                    break
    return len(sumDict)


print(driver(50000000))


runTime = datetime.now() - start

print()
print(runTime)
print()


