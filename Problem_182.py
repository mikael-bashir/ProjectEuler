from datetime import datetime
from modular import gcd


initial = datetime.now()


phi = (1009 - 1) * (3643 - 1)
p = 1009
q = 3643
total = 0
minE = phi

for e in range(2, phi):
    if gcd(e, phi) == 1:
        temp = (gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1)
        if minE > temp:
            minE, total = temp, e
        elif minE == temp:
            total += e


print(total)

runTime = datetime.now() - initial


print()
print(runTime)


