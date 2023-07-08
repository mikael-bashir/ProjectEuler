from math import tan, atan, pi, sin, asin, factorial

shoreline = []
constant = atan(3/10) * (180/pi)
for i in range(29):
    found = False
    dry = [i, 0]
    for j in range(1, 29):
        if i**2 + j**2 < 784:
            dry[1] += 1
        else:
            break
    shoreline.append(dry)

print(shoreline)
seaLine = []
for i in range(29):
    for j in range(29):
        if i**2 + j**2 >= 784:
            seaLine.append([i, j])
            break
print(seaLine)


def down(m1, m2, a):
    ratio = 1 + m2[2]/m1[2]
    horizontalDistance = ((m1[0] - m2[0])**2 + (m1[1] - m2[1])**2)**0.5
    x1 = horizontalDistance/ratio
    return x1/sin(a)

def up(m1, m2, a):
    ratio = 1 + m1[2]/m2[2]
    horizontalDistance = ((m1[0] - m2[0])**2 + (m1[1] - m2[1])**2)**0.5
    x2 = horizontalDistance/ratio
    return x2/sin(a)



possiblePeaks = [[2, 17, 21], [2, 21, 17], [3, 7, 26], [3, 10, 25], [3, 14, 23], [3, 23, 14], [3, 25, 10], [3, 26, 7], \
                [5, 15, 22], [5, 22, 15], [6, 13, 23], [6, 23, 13], [7, 3, 26], [7, 18, 19], [7, 19, 18], [7, 26, 3], \
                 [9, 13, 22], [9, 22, 13], [10, 3, 25], [10, 25, 3], [11, 17, 18], [11, 18, 17], [13, 6, 23], \
                 [13, 9, 22], [13, 22, 9], [13, 23, 6], [14, 3, 23], [14, 23, 3], [15, 5, 22], [15, 22, 5], [17, 2, 21],\
                 [17, 11, 18], [17, 18, 11], [17, 21, 2], [18, 7, 19], [18, 11, 17], [18, 17, 11], [18, 19, 7], \
                 [19, 7, 18], [19, 18, 7], [21, 2, 17], [21, 17, 2], [22, 5, 15], [22, 9, 13], [22, 13, 9], \
                 [22, 15, 5], [23, 3, 14], [23, 6, 13], [23, 13, 6], [23, 14, 3], [25, 3, 10], [25, 10, 3], [26, 3, 7], \
                 [26, 7, 3]]

actualPeaks = []

maxAlpha = 0
minAlpha = pi/2
for i in possiblePeaks:
    alpha = atan((i[2]*0.1875)/(29-(i[0]**2 + i[1]**2)**0.5))
    if alpha > maxAlpha:
        maxAlpha = alpha
    if alpha < minAlpha:
        minAlpha = alpha

print(minAlpha, maxAlpha, atan(3/10))
finalPeaks = []
calculatedAlpha = asin(3/5)
for i in possiblePeaks:
    if (((i[2]*0.1875)/tan(calculatedAlpha)) + ((i[0]**2 + i[1]**2)**0.5)) < 29:
        actualPeaks.append(i)

length = len(actualPeaks)
for i in range(length):
    if (actualPeaks[i][1] - (actualPeaks[i][2]/tan(calculatedAlpha)))>0 and (actualPeaks[i][0] - (actualPeaks[i][2]/tan(calculatedAlpha)))>0:
        finalPeaks.append(i)

def time():


'''
3, 25, 10
3, 26, 7
'''