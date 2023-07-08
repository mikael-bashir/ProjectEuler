
from itertools import combinations
from datetime import datetime

now = datetime.now()
min = None
min1 = 0
min2 = 0


def isPent(n):
    temp = (1+((1+(24*n))**(1/2)))/6
    if temp == int(temp):
        return True
    else:
        return False


def nPent(n):
    return int(((n*((3*n)-1))/2))


def abs(n):
    if n < 0:
        n = -n
    return n

first100 = []

for i in range(1, 10001):
    first100.append(nPent(i))

comb = list(combinations(first100, 2))
for i in comb:
    i = list(i)
    sum = i[0]+i[1]
    dif = abs(i[0] - i[1])
    if isPent(dif) and isPent(sum):
        if min == None:
            min = dif
            min1 = i[0]
            min2 = i[1]
        else:
            if dif < min:
                min = dif
                min1 = i[0]
                min2 = i[1]


print(min, min1, min2)
run_time = datetime.now() - now
print(len(comb))


print(run_time)


