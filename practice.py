from datetime import datetime
import math

initial = datetime.now()


def analyse(y, top, bottom):
    for power in range(1, 8):
        a = 1
        b = 1
        approx = top / bottom
        for i in range(10 ** power):
            if approx < y:
                approx *= top
                a += 1
            else:
                approx = approx / bottom
                b += 1
        print(a / b)


y = 1
t = 1
b = 0.1
analyse(y, t, b)

runTime = datetime.now() - initial

print()
print(runTime)
print()

second = datetime.now()


def model(b, t):
    try:
        if b < -1:
            b = -b
        if t < -1:
            t = -t
        print(math.log(b, t))
    except:
        print('out of domain')


model(b, t)

secondTime = datetime.now() - second

print()
print(secondTime)

# ========================================
# general behaviour of system
# ========================================
#
# model works well whenever b and t both > 1
# model works well whenever b and t both < 1
# when model works, y doesn't affect a / b
# if 0 < b < t < 1, then converges to 0, model fails
# model fails if t = 1 or b = 1

