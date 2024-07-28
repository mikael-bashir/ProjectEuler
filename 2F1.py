from datetime import datetime
import modular
from math import factorial, comb

initial = datetime.now()


def specialF(b, c):
    # a = 1, z = 0.5, n > m > 1, integer pair (n, m)
    n = b+1
    m = c
    y = 0
    for k in range(m+1):
        y += comb(n, k)
    temp = ((-2*(m**2) + m*(n+1) + (n-1)*n)/(factorial(m)*factorial(n-m)))+((2**(n) - y)/(factorial(n-2)))
    temp *= 0.5*factorial(m-1)*factorial(n-m-1)
    return temp


print(specialF(4, 3))

runTime = datetime.now() - initial

print()
print(runTime)



