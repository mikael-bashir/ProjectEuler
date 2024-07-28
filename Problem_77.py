from datetime import datetime
from sympy import primerange, isprime

initial = datetime.now()

primes = list(primerange(2, 81))

L, target = 5000, 11
ways = [1] + [0] * target
while True:
    ways = [1] + [0] * target
    for p in primes:
        for i in range(p, target+1):
            ways[i] += ways[i-p]
    if ways[target] > L:
        print(target)
        break
    target += 1




runTime = datetime.now() - initial

print()
print(runTime)




