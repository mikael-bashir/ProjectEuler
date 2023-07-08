from datetime import datetime
from modular import multiplicativeInverse, generalChineseRemainder


initial = datetime.now()


def amount(y, x):
    r = 1
    summ = 0
    while (x**r) < y:
        summ += y//(x**r)
        r += 1
    return summ


r83, r89, r97 = None, None, None

'''

compare = amount(10**18, 83**3)
for i in range(2, 10**7):
    if i % (10**5) == 0:
        print(i//(10**5))
    if 0 != (compare - amount(i, 83**3) - amount(10**18-i, 83**3)):
        print(i-1)
        break
CriticalValue = 502096

compare = amount(10**18, 89**3)
for i in range(2, 10**7):
    if i % (10**5) == 0:
        print(i//(10**5))
    if 0 != (compare - amount(i, 89**3) - amount((10**18, 89**3)-i)):
        print(i-1)
        break
CriticalValue = 585022

compare = amount(10**18, 97**3)
for i in range(2, 10**7):
    if i % (10**5) == 0:
        print(i//(10**5))
    if 0 != (compare - amount(i, 97**3) - amount(10**18-i, 97**3)):
        print(i-1)
        break
CriticalValue = 882983

'''


n = 10**18
# critical values:
502096
585022
882983
#  currently, there is a problem when i is a multiple of 83**3 / 89**3 / 97**3

r83 = 0 + pow(n, n, 83**3)  # k = 0 and n
last = n % (83**3)
r83 += last*(1+pow(n-1, n, 83**3))  # k = 1 and n-1
for i in range(2, 502096+1):
    last = ((last * (n - i)) // i)
    if i % (83 ** 3) != 0:
        r83 += last * pow(i, n, 83 ** 3)
    if (502096-i) % (83**3) != 0:
        r83 += last * pow(502096-i, n, 83**3)
    r83 = r83 % (83**3)
print(r83)

r89 = 0 + pow(n, n, 89**3)  # k = 0 and n
last = n % (89**3)
r89 += last*(1+pow(n-1, n, 89**3))  # k = 1 and n-1
for i in range(2, 585022+1):
    last = ((last * (n - i)) // i)
    if i % (89**3) != 0:
        r83 += last * pow(i, n, 89 ** 3)
    if (585022-i) % (89**3) != 0:
        r89 += last * pow(585022-i, n, 89**3)
    r89 = r89 % (89**3)
print(r89)

r97 = 0 + pow(n, n, 97**3)  # k = 0 and n
last = n % (97**3)
r97 += last*(1+pow(n-1, n, 97**3))  # k = 1 and n-1
for i in range(2, 882983+1):
    last = ((last * (n - i)) // i)
    if i % (97 ** 3) != 0:
        r97 += last * pow(i, n, 97 ** 3)
    if (882983-i) % (97**3) != 0:
        r97 += last * pow(882983-i, n, 97**3)
    r97 = r97 % (97**3)
print(r97)

print()
print(generalChineseRemainder([r83, r89, r97], [83**3, 89**3, 97**3]))

runTime = datetime.now() - initial

print()
print(runTime)

390110
376856
175392

(81001427414424973, 367891284947698819)

