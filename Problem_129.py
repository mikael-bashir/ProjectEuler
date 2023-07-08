from datetime import datetime
import math


start = datetime.now()


def r(k):
    result = 0
    for i in range(k):
        result += 10 ** i
    return result


def a(n):
    congruent = 0
    k = 0
    while True:
        congruent += pow((10 % n), k, n)
        congruent = pow(congruent, 1, n)
        k += 1
        if congruent == 0:
            break
    return k



cycle = 1
for i in range(500_000, 501_000):
    cycle += 1
    cycle = cycle % 5
    index = 2*i - 1
    if cycle != 0:
        print(index)
        if a(index) > 1_000_000:
            print(index)
            break

# seems that smallest n such that a(n) exceeds x is at least x, requires
# further investigation, interesting conjecture


runTime = datetime.now() - start

print()
print(runTime)
print()


