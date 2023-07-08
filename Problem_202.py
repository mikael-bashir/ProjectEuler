from datetime import datetime
from modular import gcd, generalChineseRemainder
from sympy.ntheory import factorint, mobius, totient, isprime, divisors
from sympy.ntheory.modular import crt
from itertools import combinations


# the main idea that I use to solve this problem, is instead of the ray reflecting, it continues on a straight line,
# across another equilateral triangle, in fact the previous triangle reflected across the boundary edge. This
# reflection is done until the ray hits a vertex, in a straight path. Doing this also gives that at each level
# in this infinite triangular grid requires 2 more reflections to reach then the lower level, due to the geometry
# of the grid. Also, because of the geometry, the vertices change the same way, independent of the path taken by the ray
# so if the ray is incident at angle x and another angle y, vertices C on reflected triangles will not change position.
# This makes everything easy, and the main problem now is trying to figure out if a vertex at a particular level
# is blocked by a vertex at a lower level, or if there is a smaller similar triangle. This is tough as the grid points
# are not rectangular, so you can't simply check the gcd of the coordinates of a vertex.
# modelling the distance between 3 vertices as 2, means that the above problem reduces to:
# find all positive integers not greater than 2_002_939_858, and co-prime to 6_008_819_575. I used an algorithm from
# https://math.stackexchange.com/questions/3158012/count-integers-not-greater-than-a-coprime-to-b/3158036#3158036
# to solve the above problem.

start = datetime.now()

def f(a, b):
    counter = 0
    nums = divisors(b)
    for num in nums:
        counter += (mobius(num) * int(a/num))
    return counter

level = 55
print(int((level-2)/3))
print(f(int((level-2)/3), level) - int(int((level-2)/3)/2))
print(f(2_002_939_858, 6_008_819_575))


print(totient(6_008_819_575)/3)
print()

print(factorint(int((12017639147+3)/2)))
factors = [5, 5, 11, 17, 23, 29, 41, 47]
factorCombs = []
productCombs = []
productFactors = {}
for i in range(1, len(factors)):
    temp = list(combinations(factors, i))
    for j in temp:
        product = 1
        for k in j:
            product *= k
        productFactors.update({product: j})

print(len(productFactors))
seen = {}
notValid = {}
totalNotValid = 0
progress = 0

for i in productFactors:
    temp1, temp2 = generalChineseRemainder([3, i], [6, 2*i])
    # appears to count points more than once
    # temp1, temp2 = crt([6, 2 * i], [3, i]), both yield the same result
    notValid.update({int(6_008_819_574/temp2) + int(pow(6_008_819_574, 1, temp2)/temp1): temp1})



temp9 = len(seen)
for i in notValid:
    totalNotValid += i
print(totalNotValid, temp9)

print(notValid)
print(int((3_004_409_787+1)/3), totalNotValid)
print(2*(int((3_004_409_787+1)/3) - totalNotValid))



















# reflections =
# 12_017_639_147
# level =
# 6_008_819_575
# vertices either side =
# 3_004_409_788
# 309_213_100
# last vertex =
# 3_004_409_787
# middle to last vertex length =
# 6_008_819_573
# transformed length =
# 2_002_939_858
# this length is probably wrong
runTime = datetime.now() - start
print()
print(runTime)

# answer is 1_209_002_624
#2result is 1_436_768_314
#1result is 1_384_513_658

