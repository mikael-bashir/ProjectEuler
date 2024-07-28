from datetime import datetime
from math import factorial
"https://math.stackexchange.com/questions/217597/number-of-ways-to-write-n-as-a-sum-of-k-nonnegative-integers"

initial = datetime.now()


def p(n, k):
    if (k > n) or (n == 0):
        return 0
    if k == n:
        return 1
    return p(n-1, k-1) + p(n-1, k)


n = 1
while True:
    Fn = 0
    for k in range(1, n+1):
        Fn += p(n, k)
    print(n, Fn)
    if n > 10:
        break
    n += 1


runTime = datetime.now() - initial

print()
print(runTime)




