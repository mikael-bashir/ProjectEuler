from datetime import datetime
from sympy import primerange


# must be the most painful problem so far, there must've been a lazier way to create dictionary or solve problem

initial = datetime.now()


numToSave = {
        0: {0: 12, 1: 4, 2: 8, 3: 8, 4: 6, 5: 8, 6: 10, 7: 8, 8: 12, 9: 10},
        1: {0: 4, 1: 4, 2: 2, 3: 4, 4: 4, 5: 2, 6: 2, 7: 4, 8: 4, 9: 4},
        2: {0: 8, 1: 2, 2: 10, 3: 8, 4: 4, 5: 6, 6: 8, 7: 4, 8: 10, 9: 8},
        3: {0: 8, 1: 4, 2: 8, 3: 10, 4: 6, 5: 8, 6: 8, 7: 6, 8: 10, 9: 10},
        4: {0: 6, 1: 4, 2: 4, 3: 6, 4: 8, 5: 6, 6: 6, 7: 6, 8: 8, 9: 8},
        5: {0: 8, 1: 2, 2: 6, 3: 8, 4: 6, 5: 10, 6: 10, 7: 6, 8: 10, 9: 10},
        6: {0: 10, 1: 2, 2: 8, 3: 8, 4: 6, 5: 10, 6: 12, 7: 6, 8: 12, 9: 10},
        7: {0: 8, 1: 4, 2: 4, 3: 6, 4: 6, 5: 6, 6: 6, 7: 8, 8: 8, 9: 8},
        8: {0: 12, 1: 4, 2: 10, 3: 10, 4: 8, 5: 10, 6: 12, 7: 8, 8: 14, 9: 12},
        9: {0: 10, 1: 4, 2: 8, 3: 10, 4: 8, 5: 10, 6: 10, 7: 8, 8: 12, 9: 12}
}


def oneStepDigitSum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


def countTransitionsSaved(a, b):
    global numToSave
    a, b = str(a), str(b)
    lenA, lenB = len(a), len(b)
    saved = 0
    last = 0
    if lenA > lenB:
        for i in range(lenB):
            last = numToSave.get(int(a[-i-1])).get(int(b[-i-1]))
            saved += last
    else:
        for i in range(lenA):
            last = numToSave.get(int(a[-i-1])).get(int(b[-i-1]))
            saved += last
    return saved


print(countTransitionsSaved(137, 11) + countTransitionsSaved(11, 2))


runTime = datetime.now() - initial


print()
print(runTime)


