from datetime import datetime
from sympy import primerange, isprime
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular
from collections import Counter

initial = datetime.now()

#part 1

handsRank = []

def power(a, b):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    A, B = Counter(a), Counter(b)
    temp = []
    for i in A:
        temp.append([i, A[i]])
    A = temp
    temp = []
    for i in B:
        temp.append([i, B[i]])
    B = temp
    nums1 = []
    nums2 = []
    for i in B:
        nums1.append(i[1])
    for i in A:
        nums2.append(i[1])

    if len(B) == 5:
        if len(A) <= 4:
            return True
    if len(B) == 4:
        if len(A) <= 3:
            return True
    if (len(B) == 2) and not (1 in nums1):
        if ((len(A) == 2) and (1 in nums2)) or (len(A) == 1):
            return True
    if (len(B) == 2) and not (2 in nums1):
        if len(A) == 1:
            return True
    if (len(B) == 3) and not (3 in nums1):
        if (len(A) <= 2) or ((len(A) == 3) and not (2 in nums2)):
            return True
    if (len(B) == 3) and not (2 in nums1):
        if len(A) <= 2:
            return True

    if len(A) == 5:
        if len(B) <= 4:
            return False
    if len(A) == 4:
        if len(B) <= 3:
            return False
    if (len(A) == 2) and not (1 in nums2):
        if ((len(B) == 2) and (1 in nums1)) or (len(B) == 1):
            return False
    if (len(A) == 2) and not (2 in nums2):
        if len(B) == 1:
            return False
    if (len(A) == 3) and not (3 in nums2):
        if (len(B) <= 2) or ((len(B) == 3) and not (2 in nums1)):
            return False
    if (len(A) == 3) and not (2 in nums2):
        if len(B) <= 2:
            return False

    for i in range(len(a)):
        if cards.index(a[i]) < cards.index(b[i]):
            return True
        if cards.index(b[i]) < cards.index(a[i]):
            return False


with open('day_7.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        line[1] = int(line[1])
        handsRank.append(line)

for i in range(len(handsRank)):
    for j in range(len(handsRank) - i - 1):
        if power(handsRank[j][0], handsRank[j+1][0]):
            handsRank[j], handsRank[j+1] = handsRank[j+1], handsRank[j]

winnings = 0

for i in range(len(handsRank)):
    winnings += (i+1) * handsRank[i][1]

print(winnings)

#part 2

handsRank = []

def order(a, b):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    A, B = Counter(a), Counter(b)
    ta, tb = A, B
    if len(ta) != 1:
        try:
            t = ta.get('J')
            ra = []
            for i in ta:
                if i != 'J':
                    ra.append(ta[i])
            ma = max(ra)
            for i in A:
                if (A[i] == ma) and (i != 'J'):
                    del A['J']
                    A[i] += t
                    a.replace('J', A[i])
                    break
        except:
            pass

    if len(tb) != 1:
        try:
            t = tb.get('J')
            rb = []
            for i in tb:
                if i != 'J':
                    rb.append(tb[i])
            mb = max(rb)
            for i in B:
                if (B[i] == mb) and (i != 'J'):
                    del B['J']
                    B[i] += t
                    b.replace('J', B[i])
                    break
        except:
            pass

    temp = []
    for i in A:
        temp.append([i, A[i]])
    A = temp
    temp = []
    for i in B:
        temp.append([i, B[i]])
    B = temp
    nums1 = []
    nums2 = []
    for i in B:
        nums1.append(i[1])
    for i in A:
        nums2.append(i[1])






    if len(B) == 5:
        if len(A) <= 4:
            return True
    if len(B) == 4:
        if len(A) <= 3:
            return True
    if (len(B) == 2) and not (1 in nums1):
        if ((len(A) == 2) and (1 in nums2)) or (len(A) == 1):
            return True
    if (len(B) == 2) and not (2 in nums1):
        if len(A) == 1:
            return True
    if (len(B) == 3) and not (3 in nums1):
        if (len(A) <= 2) or ((len(A) == 3) and not (2 in nums2)):
            return True
    if (len(B) == 3) and not (2 in nums1):
        if len(A) <= 2:
            return True

    if len(A) == 5:
        if len(B) <= 4:
            return False
    if len(A) == 4:
        if len(B) <= 3:
            return False
    if (len(A) == 2) and not (1 in nums2):
        if ((len(B) == 2) and (1 in nums1)) or (len(B) == 1):
            return False
    if (len(A) == 2) and not (2 in nums2):
        if len(B) == 1:
            return False
    if (len(A) == 3) and not (3 in nums2):
        if (len(B) <= 2) or ((len(B) == 3) and not (2 in nums1)):
            return False
    if (len(A) == 3) and not (2 in nums2):
        if len(B) <= 2:
            return False

    for i in range(len(a)):
        if cards.index(a[i]) < cards.index(b[i]):
            return True
        if cards.index(b[i]) < cards.index(a[i]):
            return False


with open('day_7.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        line[1] = int(line[1])
        handsRank.append(line)

for i in range(len(handsRank)):
    for j in range(len(handsRank) - i - 1):
        if order(handsRank[j][0], handsRank[j+1][0]):
            handsRank[j], handsRank[j+1] = handsRank[j+1], handsRank[j]

winnings = 0

for i in range(len(handsRank)):
    print(i+1, handsRank[i])
    winnings += (i+1) * handsRank[i][1]

print(winnings)
print()

runTime = datetime.now() - initial

print()
print(runTime)



