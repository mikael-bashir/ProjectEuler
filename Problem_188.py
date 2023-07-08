from datetime import datetime
from sympy import primefactors, primerange
from modular import totient


# made heavy use of euler's theorem, very efficient, on the downside very specialised code, doesn't look for solution \
# it's self

initial = datetime.now()


temp = 0
mod = 2
remainder = 1


for i in range(24, 8, -1):
    temp = remainder
    remainder = pow(1777, remainder, mod)
    print('(level', str(i) + ')', 1777, '^', temp, '(mod', str(mod) + ')', '=', remainder)
    mod *= 2


print()
mod = int(mod/8)  # dividing by an extra 2 because last step of above loop multiplies by 2
mod *= 10

for i in range(8, 1, -1):
    temp = remainder
    remainder = pow(1777, remainder, mod)
    print('(level', str(i) + ')', 1777, '^', temp, '(mod', str(mod) + ')', '=', remainder)
    mod = int(mod/4)
    mod *= 10

print()
print(pow(1777, remainder, 10**8))


runTime = datetime.now() - initial


print()
print(runTime)


