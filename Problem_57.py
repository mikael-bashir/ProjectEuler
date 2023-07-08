from datetime import datetime

initial = datetime.now()


def countExpansion(lim):
    count = 0
    a = 3
    b = 2
    for i in range(2, lim+1):
        a, b = a + 2*b, a + b
        if len(str(a)) > len(str(b)):
            count += 1
    return count


print(countExpansion(1000))

runTime = datetime.now() - initial

print()
print(runTime)
