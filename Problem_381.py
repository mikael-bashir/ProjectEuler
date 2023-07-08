from datetime import datetime
from modular import multiplicativeInverse
from sympy import primerange


# not efficient, 2 minutes 30 seconds


initial = datetime.now()


def S(p):
    total = 0
    sign = -1
    multiplier = 1
    for k in range(1, 6):
        factorial = multiplier * sign
        if k < 3:
            total += factorial % p
        else:
            total += multiplicativeInverse(factorial, p)
        multiplier *= k
        sign *= -1
    return total % p


def sigma(n):
    total = 0
    for p in primerange(2, n+1):
        total += S(p)
    return total


answer = 0
for p in primerange(5, 10**8):
    answer += S(p)

print(answer)

runTime = datetime.now() - initial


print()
print(runTime)
print()


