from datetime import datetime
from sympy import primefactors


initial = datetime.now()


def R(k):
    result = 0
    for i in range(k):
        result += 10 ** k
    return result


for num in range(1, 100):
    temp = primefactors(R(num))
    print(temp, R(num))


runTime = datetime.now() - initial


print()
print(runTime)


