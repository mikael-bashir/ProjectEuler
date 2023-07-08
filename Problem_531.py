from datetime import datetime
from sympy.ntheory import factorint
from itertools import combinations
from modular import multiplicativeInverse, multilcm, generalChineseRemainder, lcm
from sympy import factorial, primerange, totient
from math import tan, atan


def gcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    g = b
    return g

start = datetime.now()


totientCache = []
for i in range(1_000_000, 1_005_000):
    totientCache.append(totient(i))

sum = 0


for m in range(1_000_001, 1_005_000):
    b = totientCache[m - 1_000_000]
    for n in range(1_000_000, m):
        g = gcd(n, m)

        a = totientCache[n - 1_000_000]

        if (b - a) % g != 0:
            continue

        sum += n * ((multiplicativeInverse(int(n / g), int(m / g)) * (int((b - a) / g))) % int(m / g)) + a


print(sum)
runTime = datetime.now() - start

print()
print(runTime)
print()

4629416843813025681
4515432351156203105
4.5154323511553475