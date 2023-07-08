from datetime import datetime
from sympy import isprime


# 10 seconds, pretty good

initial = datetime.now()


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


count = 0
total = 0
for n in range(3, 100000):
    if n % 2 != 0 and n % 5 != 0:
        if not isprime(n):
            if (n-1) % a(n) == 0:
                count += 1
                total += n
                print(n, count)
    if count > 24:
        break


print()
print(total)


runTime = datetime.now() - initial


print()
print(runTime)


