from math import asin, pi
from datetime import datetime

# --------------------------------------
# manual binary search on a sensible interval quickly reveals 2240 is the answer
# --------------------------------------

now = datetime.now()


def A(n):
    m = 1/n
    return (m+1-((2*m)**0.5))/((m**2)+1)


def areaRatio(n):
    m = 1/n
    a = (m+1-((2*m)**0.5))/((m**2)+1)
    return (((0.5*(a**2)*m) + (1-a) + (0.5*(a-1)*((1-((a-1)**2))**0.5)) + (0.5*asin(a-1)))/(1-(pi/4)))*100


print(areaRatio(2239))
print(areaRatio(2240))

runTime = datetime.now() - now
print(runTime)