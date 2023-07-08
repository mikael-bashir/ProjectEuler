from datetime import datetime
from math import factorial
from modular import generalChineseRemainder
from hyperop import hyperop


start = datetime.now()


def trashA(m, n):
    if m == 0:
        return n + 1
    if (m>0) and (n==0):
        return trashA(m-1, 1)
    if (m>0) and (n>0):
        return trashA(m-1, trashA(m, n-1))


def optimalA(m, n):
    H = hyperop(m)
    return H(2, n+3) - 3


print(optimalA(0, 0))
print(optimalA(1, 1))
print(optimalA(2, 2))
print(optimalA(3, 3))


# --------------------------------
# A(4, 4) (mod 14**8)
# --------------------------------

power = generalChineseRemainder([-1, 0, 2], [3, 2, 49])[0]
for i in range(2, 7):
    power = generalChineseRemainder([1, 0, pow(2, power, 7**(i+1))], [3, 2, 7**(i+1)])[0]

A4 = generalChineseRemainder([0, pow(2, power, 7**8)], [2**8, 7**8])[0]-3
print(A4)


# --------------------------------
#
# --------------------------------


# --------------------------------
# A(5, 5) (mod 14**8)
# --------------------------------


power = generalChineseRemainder([1, 0], [3, 2])[0]
for i in range(1, 8):
    power = generalChineseRemainder([1, 0, pow(2, power, 7**i)], [3, 2, 7**i])[0]
A5 = generalChineseRemainder([0, pow(2, power, 7**8)], [2**8, 7**8])[0]-3
print(A5)


# --------------------------------
#
# --------------------------------


# --------------------------------
# A(6, 6) (mod 14**8)
# --------------------------------


power = generalChineseRemainder([1, 0], [3, 2])[0]
for i in range(1, 8):
    power = generalChineseRemainder([1, 0, pow(2, power, 7**i)], [3, 2, 7**i])[0]
A6 = generalChineseRemainder([0, pow(2, power, 7**8)], [2**8, 7**8])[0]-3
print(A6)


# --------------------------------
#
# --------------------------------

print()
print((1+3+7+61+A4+A5+A6) % (14**8), 14**8)


runTime = datetime.now()-start

print()
print(runTime)
