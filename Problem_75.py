from datetime import datetime
from math import sqrt
from collections import defaultdict

start = datetime.now()


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def zero():
    return 0


def generateTriplets(m):  # Euclid's formula
    lengths = defaultdict(zero)
    answer = 0
    for i in range(2, int(sqrt(m / 2)) + 1):
        for j in range(1, i):
            if gcd(i, j) == 1 and (i + j) % 2 == 1:
                a = i ** 2 - j ** 2
                b = 2 * i * j
                c = i ** 2 + j ** 2
                total = a + b + c
                for k in range(1, (m // total) + 1):
                    lengths[k * total] += 1
    for i in lengths:
        if lengths[i] == 1:
            answer += 1
    print(answer)


generateTriplets(1500000)

runTime = datetime.now() - start

print()
print(runTime)
print()


