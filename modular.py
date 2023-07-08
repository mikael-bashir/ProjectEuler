from sympy import primefactors
from sympy.ntheory import factorint
from itertools import combinations


def gcd(a, b, small=True):  # tested a lot, reliable
    if small:
        while b:
            a, b = b, a%b
        return a
    else:
        while b:
            a, b = b, pow(a, 1, b)
        return a


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def multigcd(a, nums):  # not efficient, iterative approach better than recursive
    b = nums[0]
    if len(nums) == 1:
        while b:
            a, b = b, a % b
        return a
    else:
        nums.remove(b)
        while b:
            a, b = b, a % b
        return multigcd(a, nums)


def multiplicativeInverse(a, n):  # tested a fair amount, has been reliable
    s, t, nextS, nextT = n, 0, a, 1

    while nextS:
        wholeDiv = s // nextS
        t, nextT = nextT, t - wholeDiv * nextT
        s, nextS = nextS, s - wholeDiv * nextS

    if s > 1 or s < 1:
        return 0
        # print('a does not have a multiplicative inverse')
    if t < 0:
        t = t + n
    if a * n < 0:
        return n - t
    return t


def chineseRemainder(remainderL, modulusL) -> tuple:  # for co-prime moduli only
    N = 1
    x = 0
    for i in modulusL:
        N *= i
    for i in range(len(modulusL)):
        n = modulusL[i]
        y = N // n
        x += remainderL[i] * y * multiplicativeInverse(y, n)
    return x % N, N


def generalChineseRemainder(remainders, moduli) -> tuple:  # reliable
    # ------------------------------------------
    # requires factorization
    # ------------------------------------------
    lengthRemainder = len(remainders)
    if lengthRemainder == len(moduli):
        if lengthRemainder != 0:
            # --------------
            # check if system is pairwise co-prime
            # --------------
            isPairwiseCoprime = True
            pairs = combinations(moduli, 2)
            for pair in pairs:
                if gcd(pair[0], pair[1]) != 1:
                    isPairwiseCoprime = False
                    break
            # --------------
            # end of check
            # --------------
            if isPairwiseCoprime:
                # --------------
                # normal chinese implementation
                # --------------
                N = 1
                x = 0
                for i in moduli:
                    N *= i
                for i in range(lengthRemainder):
                    n = moduli[i]
                    y = N // n
                    x += remainders[i] * y * multiplicativeInverse(y, n)
                return x % N, N
                # --------------
                # end of normal implementation
                # --------------
            else:
                # --------------
                # checking if there exists a solution
                # --------------
                isPossible = True
                congruenceSystem = []
                for i in range(lengthRemainder):
                    congruenceSystem.append([remainders[i], moduli[i]])
                pairs = combinations(congruenceSystem, 2)
                for pair in pairs:
                    divisor = gcd(pair[0][1], pair[1][1])
                    if pair[0][0] % divisor != pair[1][0] % divisor:
                        isPossible = False
                        break
                # --------------
                # end of check
                # --------------
                if isPossible:
                    # --------------
                    # transforming system into a pairwise co-prime system, without loss of information
                    # --------------
                    lcm = multilcm(moduli[0], moduli[1:])
                    lcmFactorization = factorint(lcm)
                    primesAvailable = list(lcmFactorization)
                    redundantIndices = []
                    for i in range(lengthRemainder):
                        modulus = moduli[i]
                        newModulus = 1
                        factorization = factorint(modulus)
                        for prime in factorization:
                            if factorization.get(prime) == lcmFactorization.get(prime) and prime in primesAvailable:
                                newModulus *= prime ** factorization.get(prime)
                                primesAvailable.remove(prime)
                        if newModulus == 1:
                            redundantIndices.append(i)
                        else:
                            moduli[i] = newModulus
                            remainders[i] = remainders[i] % newModulus
                        if len(primesAvailable) == 0:
                            moduli = moduli[0:i+1]
                            remainders = remainders[0:i+1]
                            break
                    # --------------
                    # end of transformation
                    # --------------
                    for i in redundantIndices:
                        del moduli[i]
                        del remainders[i]
                    # --------------
                    # normal chinese implementation
                    # --------------
                    N = 1
                    x = 0
                    for i in moduli:
                        N *= i
                    for i in range(len(moduli)):
                        n = moduli[i]
                        y = N // n
                        x += remainders[i] * y * multiplicativeInverse(y, n)
                    return x % N, N
                    # --------------
                    # end of normal implementation
                    # --------------
                else:
                    # --------------
                    # commands if no solution exists
                    # --------------
                    # raise ValueError("generalChineseRemainder(X, Y): there doesn't exist a solution to the system")
                    return 0, 0
        else:
            raise ValueError("generalChineseRemainder(X, Y): X and Y must not be empty!")
    else:
        raise ValueError("generalChineseRemainder(X, Y): X and Y must be of the same size!")


def advancedChineseRemainder(remainders, moduli) -> tuple:  # for a double congruence system only
    # ------------------------------------------
    # requires factorization
    # ------------------------------------------
    isCoprime = True
    if gcd(moduli[0], moduli[1]) != 1:
        isCoprime = False
    if isCoprime:
        remainOne = remainders[0]
        modTwo = moduli[1]
        remainTwo = remainders[1]
        modOne = moduli[0]
        x = remainOne * modTwo * multiplicativeInverse(modTwo, modOne)
        x += remainTwo * modOne * multiplicativeInverse(modOne, modTwo)
        return x % (modTwo * modOne)
    else:
        isPossible = True
        divisor = gcd(moduli[0], moduli[1])
        multiple = lcm(moduli[0], moduli[1])
        if (remainders[0] % divisor) != (remainders[1] % divisor):
            isPossible = False
        if isPossible:
            product = multilcm(moduli[0], moduli[1:])
            lcmFactorization = factorint(product)
            primesAvailable = list(lcmFactorization)
            redundantIndices = []
            for i in range(len(remainders)):
                modulus = moduli[i]
                newModulus = 1
                factorization = factorint(modulus)
                for prime in factorization:
                    if factorization.get(prime) == lcmFactorization.get(prime) and prime in primesAvailable:
                        newModulus *= prime ** factorization.get(prime)
                        primesAvailable.remove(prime)
                if newModulus == 1:
                    redundantIndices.append(i)
                else:
                    moduli[i] = newModulus
                    remainders[i] = remainders[i] % newModulus
                if len(primesAvailable) == 0:
                    moduli = moduli[0:i + 1]
                    remainders = remainders[0:i + 1]
                    break
            remainOne = remainders[0]
            modTwo = moduli[1]
            remainTwo = remainders[1]
            modOne = moduli[0]
            x = remainOne * modTwo * multiplicativeInverse(modTwo, modOne)
            x += remainTwo * modOne * multiplicativeInverse(modOne, modTwo)
            return x % (modTwo * modOne)
        else:
            return 0


def generalEasyCRT(remainders, moduli) -> tuple:
    # ------------------------------------------
    # doesn't require factorization, https://math.stackexchange.com/questions/20223/solving-ge-2-congruences-by-crt-chinese-remainder-theorem/20259#20259
    # ------------------------------------------
    length = len(remainders)
    a, m = remainders[0], moduli[0]
    for i in range(1, length):
        b, n = remainders[i], moduli[i]
        d = gcd(n, m)
        if (b-a)%d == 0:
            a, m = (a+(m*((((b-a)//d)*multiplicativeInverse((m//d), (n//d)))%(n//d))))%((m*n)//d), ((m*n)//d)
        else:
            return 0, 0
    return a%m, m


def lcm(a, b):
    return (a // gcd(a, b)) * b


def multilcm(a, nums):  # not efficient, iterative approach better than recursive
    b = nums[0]
    if len(nums) == 1:
        return (a // gcd(a, b)) * b
    else:
        a = (a // gcd(a, b)) * b
        nums.remove(b)
        return multilcm(a, nums)


def totient(n):  # tested a lot, reliable
    totient = n
    fList = factorint(n)
    for prime in fList:
        totient *= (prime - 1)
        totient = totient // prime
    return totient


def tetrationMod(a, t, n):  # currently, only for prime a, this is suspected to not work
    temp = totient(n)
    divisorTower = [a]
    modulusTower = [n]
    level = 1
    while temp > 2 and level < t:
        level += 1
        temp = totient(temp)  # may have missed that totient may not be co-prime to a, and should use CRT, possible point of failure
        divisorTower.append(a)
        modulusTower.append(temp)
    power = 1
    upper = len(divisorTower)
    for i in range(upper-1, -1, -1):
        power = pow(divisorTower[i], power, modulusTower[i])
    return power


def updatedTetrationMod(a, t, n):
    pass



def factorialMod(a, n):
    pass


def hyperoperatorMod(a, b, n, modulus):  # only for powers and higher ranks
    pass

