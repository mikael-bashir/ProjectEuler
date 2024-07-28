from datetime import datetime


initial = datetime.now()


def main():
    numDen = []
    n = 99
    num = 1
    for i in range(0, n):
        if i%3 == 0:
            numDen.append(1)
        if i%3 == 1:
            temp = (i+2)//3
            numDen.append(2*temp)
        if i%3 == 1:
            numDen.append(1)
    den = numDen[n-1]
    for i in range(0, n-1):
        i = n-2-i
        temp = numDen[i]
        num = (temp*den)+num
        num, den = den, num

    num = (2*den)+num

    print(num, den)

    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)


main()

runTime = datetime.now() - initial



print()
print(runTime)




