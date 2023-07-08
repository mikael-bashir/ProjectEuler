from datetime import datetime

initial = datetime.now()

def isPal(num):
    return num == num[::-1]

pal = []
for i in range(1, 100000000):
    if isPal(str(i)):
        pal.append(i)

run_time = datetime.now() - initial

print(run_time)

a, b, c, d = 2, 5, 3, 7

