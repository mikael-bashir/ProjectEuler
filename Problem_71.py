from datetime import datetime
from sympy import primefactors

initial = datetime.now()

answer = 0


def totient(n, arr):
    for i in arr:
        n *= (1 - (1/i))
    return int(n)


for i in range(1, 1000001):
    print(i)
    answer += totient(i, primefactors(i))
    # this will add the totient of 1, however there isn't any reduced fraction for d = 1



print()
print(answer - 1)


run_time = datetime.now() - initial
print()
print(run_time)

303963552391

