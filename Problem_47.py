from sympy import primefactors
from datetime import datetime

now = datetime.now()

index = 1
stop = False

while True:
    a = primefactors(index)
    b = primefactors(index + 1)
    c = primefactors(index + 2)
    d = primefactors(index + 3)
    if (((len(a) == 4) and (len(b) == 4)) and (len(c) == 4)) and (len(d) == 4):
        if ((a != b) and (b != c)) and (a != c) and (d != a) and (d != b) and (d != c):
            stop = True
    if stop:
        print(index, a, b, c, d)
        break
    index += 1

run_time = datetime.now() - now

print(run_time)

