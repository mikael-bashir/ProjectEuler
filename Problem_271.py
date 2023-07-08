from datetime import datetime
from modular import multiplicativeInverse
from modular import gcd
from modular import generalChineseRemainder
from sympy import primerange
from itertools import combinations
from sympy.ntheory import factorint


initial = datetime.now()

# findings:
# - x must end in 1, as 13082761331670030 ends in 0.
# - 13082761331670030 is the product of the primes, 2 through 43 inclusive
# - prime factors of 13082761331670030 must divide (x - 1) or (x**2 + x + 1), or both.
# - quadratic residues may help for determining values of x for (x**2 + x + 1)

# final thoughts:
# - some ideas above were unhelpful and led me off to tangents
# - in the end I simply used CRT on the residues for each prime factor of 13082761331670030
# - pretty fast, but I didn't do a general function/program


pFactors = primerange(2, 44)

upper = 13082761331670030


def last(n):
    return str(n)[-1]

'''
def isQuadraticResidue(a, modulus):
    result = pow(a, ((modulus-1)/2), modulus)
    if result == 1:
        return True
    if result == -1:
        return False
    if result == 0:
        return False


def peel(a, p):
    # Returns (k, b) such that a = p^k * b and b is minimal.
    if a == 0: return (1, 0)
    k = 0
    while a % p == 0:
        k += 1
        a = a // p
    return (k, a)

def is_quadratic_residue(a, n):
    for p in factorint(n):
        e = factorint(n).get(p)
        (k, b) = peel(a % p**e, p)
        if b == 0: continue
        if k % 2: return False
        if p == 2:
            if e == 1: continue
            if b % 4 != 1: return False
            if e >= 3 and b % 8 != 1: return False
        else:  # Euler's criterion
            if pow(b, (p - 1)//2, p) != 1:
                return False
    return True


def specialQuadraticResidues(a, b, c, modulus):
    multiplier = multiplicativeInverse(a, modulus)
    a, b, c = a*multiplier, b*multiplier, c*multiplier
    a, b, c = a%modulus, b%modulus, c%modulus
    temp = (c - (b**2)/4)%modulus
    temp -= modulus
    if isQuadraticResidue(1 * temp, modulus):
        return True
    else:
        return False


print(generalChineseRemainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], list(primerange(2, 44))))

products = []
for size in range(1, 15):
    temp = list(combinations(list(primerange(2, 44)), size))
    for i in temp:
        product = 1
        for j in i:
            product *= j
        products.append(product)

print(len(products))

for i in products:
    if is_quadratic_residue(3, i) and (i%2 != 0):
        print(i)


print()
'''


def residues(n):
    result = []
    for x in range(1, n):
        if pow(x, 3, n) == 1:
            result.append(x)
    return result


residueList = []
uniqueCheck = {}


for factor in list(primerange(2, 44)):
    residue = residues(factor)
    residueList.append(residue)

print(residueList)


for a in residueList[0]:
    for b in residueList[1]:
        for c in residueList[2]:
            for d in residueList[3]:
                for e in residueList[4]:
                    for f in residueList[5]:
                        for g in residueList[6]:
                            for h in residueList[7]:
                                for i in residueList[8]:
                                    for j in residueList[9]:
                                        for k in residueList[10]:
                                            for l in residueList[11]:
                                                for m in residueList[12]:
                                                    for n in residueList[13]:
                                                        remainder, modulus = generalChineseRemainder([a, b, c, d, e, f,\
                                                        g, h, i, j, k, l, m, n], list(primerange(2, 44)))
                                                        uniqueCheck.update({remainder: modulus})


del uniqueCheck[1]
print(uniqueCheck)
sum = 0
for entry in uniqueCheck:
    sum += entry
print(sum)









































runTime = datetime.now() - initial


print()
print(runTime)
print()


