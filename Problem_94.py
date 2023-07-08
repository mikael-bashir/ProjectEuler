from datetime import datetime
import math


start = datetime.now()


#Project Euler Problem 94

side0, side, s, p, m = 1, 1, 0, 0, 1

L = 10**9


while p <= L:
    print(side0, side, s, p, m)
    side0, side, m = side, 4 * side - side0 + 2 * m, -m
    s += p
    p = 3 * side - m

print("Sum of perimeters less than", L, " =", s)

'''


def driver(upper):
    aPos1 = 5
    aPos2 = 65
    aNeg1 = 17
    aNeg2 = 241
    print(aPos1, aPos1, aPos1 + 1)
    print(aNeg1, aNeg1, aNeg1 - 1)
    print(aPos2, aPos2, aPos2 + 1)
    print(aNeg2, aNeg2, aNeg2 - 1)
    perimeterSum = 3 * (5 + 65 + 17 + 241)
    for i in range(upper):
        aPos2, aPos1 = (14 * aPos2) - aPos1 - 4, aPos2
        aNeg2, aNeg1 = (14 * aNeg2) - aNeg1 + 4, aNeg2
        if aPos2 > int(upper/3) or aNeg2 > int(upper/3) + 1:
            break
        print(aPos2, aPos2, aPos2 + 1, heron(aPos2, aPos2, aPos2 + 1))
        print(aNeg2, aNeg2, aNeg2 - 1, heron(aNeg2, aNeg2, aNeg2 - 1))
        perimeterSum += 3 * (aPos2 + aNeg2)
    return perimeterSum


'''

runTime = datetime.now() - start

print()
print(runTime)
print()


