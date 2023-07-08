from modular import gcd


def simplifier(a, b, small=True):
    simpleA, simpleB = a, b
    if (simpleA == int(a)) and (simpleB == int(b)):
        temp = gcd(a, b, small)
        simpleA, simpleB = int(a/temp), int(b/temp)
    else:
        tempA, tempB = str(a), str(b)
        power = max(len(tempA), len(tempB))
        simpleA, simpleB = int(a * (10 ** power)), int(b * (10 ** power))
        temp = gcd(simpleA, simpleB, small)
        simpleA, simpleB = int(simpleA/temp), int(simpleB/temp)
    return simpleA, simpleB
