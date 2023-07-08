from datetime import datetime
from sympy import primefactors, primerange, isprime, factorial
from sympy.ntheory import factorint
from modular import multiplicativeInverse, generalChineseRemainder
# very interesting finding, the number of zeros at the end of a factorial, less than n, is related to totient of 5

initial = datetime.now()


index = 1
numZero = 0
while True:
    power = 5 ** index
    if power < 1_000_000_000_000:
        numZero += int(1_000_000_000_000 / power)
        index += 1
    else:
        break


print(numZero)
print(1_000_000_000_000)



temp = pow(2*3*4, 2 * (10**6), 5**5)

print(generalChineseRemainder([0, 8], [2**5, 5**5]))
print(pow(24, 2 * (10**11), 5**5))

runTime = datetime.now() - initial


print()
print(runTime)

'''

249999999994! (mod 249999999997)

'''
