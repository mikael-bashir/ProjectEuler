from datetime import datetime

initial = datetime.now()


ex = []


with open('exponent.txt', 'r') as expo:
    for lines in expo:
        lines = lines.replace('\n', '')
        ex.append(lines.split(','))


greatest = [498005, 527503]
line = 0
for j in range(0, 1000):
    i = list(ex[j])
    if int(greatest[0]) < ((int(i[0])) ** (int(i[1]) / int(greatest[1]))):
        greatest = list(i)
        line = j + 1


print(line)



run_time = datetime.now() - initial

print()
print(run_time)
