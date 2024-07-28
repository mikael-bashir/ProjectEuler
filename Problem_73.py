from datetime import datetime
from modular import gcd
from math import floor, ceil



initial = datetime.now()


max = 12000
count = 0
for d in range(4, max+1):
    if d%3 == 0:
        lower = ceil(d/3) + 1
    else:
        lower = ceil(d/3)
    if d%2 == 0:
        upper = floor(d/2) - 1
    else:
        upper = floor(d/2)
    for i in range(lower, upper+1):
        if gcd(i, d) == 1:
            count += 1
print(count)



runTime = datetime.now() - initial



print()
print(runTime)

7298372


