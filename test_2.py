from datetime import datetime

start = datetime.now()

summ = 0
for i in range(1, 1000):
    if i%3==0:
        summ += i
    if i%5 == 0:
        summ += i
    if i%15 == 0:
        summ = summ - i

runtime = datetime.now() - start
print(summ)
print()
print(runtime)