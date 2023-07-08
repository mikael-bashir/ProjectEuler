(2969, 6299, 9629)
from sympy import isprime
from collections import Counter
from datetime import datetime

now = datetime.now()

check = (2969, 6299, 9629)


def isPerm(a, b):
    if Counter(str(a)) == Counter(str(b)):
        return True
    else:
        return False


for i in range(1, 4500):
    for j in range(1000, 10000 - (2 * i)):
        triple = []
        for count in range(0, 3):
            triple.append(j + (i * count))
        if isprime(triple[0]) and isprime(triple[1]) and isprime(triple[2]):
            if isPerm(triple[0], triple[1]) and isPerm(triple[1], triple[2]) and isPerm(triple[0], triple[2]):
                print(triple)


run_time = datetime.now() - now
print(run_time)

