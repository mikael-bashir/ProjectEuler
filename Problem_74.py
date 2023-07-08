from datetime import datetime
from math import factorial

initial = datetime.now()


def transform(n):
    result = 0
    for i in str(n):
        result += factorial(int(i))
    return result


exactChains = 0
for i in range(1_000_000):
    currentChain = 0
    chain = []
    temp = i
    while True:
        if temp not in chain:
            chain.append(temp)
            temp = transform(temp)
            currentChain += 1
        else:
            break
    if currentChain == 60:
        exactChains += 1

print(exactChains)

runTime = datetime.now() - initial


print()
print(runTime)




