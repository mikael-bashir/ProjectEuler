from datetime import datetime
from sympy import isprime

initial = datetime.now()

result = [0]
index = 1


for k in range(2, 201):
    if isprime(k):
        result.append(result[-1] + 1)
    else:
        result.append(result[-1])

for k in range(1, 9):
    result[index-1] = k-1
    index *= 2

print(result)
print(result[14])

runTime = datetime.now() - initial

print()
print(runTime)
