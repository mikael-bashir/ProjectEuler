from datetime import datetime


initial = datetime.now()


power = 1
integer = 1
answer = 0
stop = False

while True:
    for i in range(1, 10):
        temp = len(str(i**power))
        if temp == power:
            answer += 1
        elif temp > power:
            break
        elif temp < power and i == 9:
            stop = True
            break
    if stop:
        break
    power += 1

print(answer)












run_time = datetime.now() - initial

print()
print(run_time)
