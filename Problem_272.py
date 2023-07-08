from datetime import datetime
from sympy.ntheory import factorint
from itertools import combinations
from modular import gcd, multiplicativeInverse, multilcm, generalChineseRemainder
from sympy import factorial, primerange, isprime
from math import tan, atan
from math import log


start = datetime.now()


# - from experimental, it seems that the number of solutions to x**3 (mod p) = 1, is equal
# to the number of solutions to x**3 (mod p**q) = 1, for some positive integer q, no idea why.
# - this is useful as there is a formula for the number of cubic residues for a prime p, not
# - explicitly for positive integer powers of prime p - the euler criterion is very handy here.
# let q = hcf(3, p-1), then if a**((p-1)/q) (mod p) = 1, there are exactly q solutions
# from experimental it also appears that a system either has 1 or 3 residues
# we want 242 + 1 solutions = 3 ** 5. This is good as it is in line with our conjectures.
# what we have is that every set of 5 primes, or 5 prime powers, that all have 3 residuals modulo p**q,
# gives 243 solutions.

def experimental(modulus):
    result = []
    for i in range(1, modulus):
        if pow(i, 3, modulus) == 1:
            result.append(i)
    return result


print(len(experimental(85)))

runTime = datetime.now() - start

print()
print(runTime)
for i in range(1, 100):
    if not isprime(i) and len(experimental(i)) == 3:
        print(i)

50424


