from datetime import datetime
from sympy import primefactors


# 16 minutes, need to optimize or change algorithm

start = datetime.now()


def totient(n):
    pFactors = primefactors(n)
    result = n
    for i in pFactors:
        result *= (i - 1)
        result = result / i
    return int(result)


def rMax(a):
    maximum = 0
    for n in range(1, totient(a ** 2) + 1):
        temp = (pow(a-1, n, a**2) + pow(a+1, n, a**2)) % (a**2)
        if temp > maximum:
            maximum = temp
    return maximum


total = 0
print(rMax(7))
for i in range(3, 1001):
    total += rMax(i)
print(total)


runTime = datetime.now() - start

print()
print(runTime)
print()


