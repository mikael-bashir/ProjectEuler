from datetime import datetime
from sympy import isprime


# 2 minutes 15 seconds, decent time

start = datetime.now()


total = 0
for i in range(1, 15000001):
    num = i * 10
    if (num % 3 != 0) and (num % 7 != 0) and (num % 13 != 0):
        n = num ** 2
        if isprime(n+1) and isprime(n+3) and isprime(n+7) and isprime(n+9) and isprime(n+13) and isprime(n+27):
            if not isprime(n+11) and not isprime(n+17) and not isprime(n+19) and not isprime(n+21)\
                    and not isprime(n+23):
                total += num
                print(num)

print()
print(total)


runTime = datetime.now() - start

print()
print(runTime)
print()


