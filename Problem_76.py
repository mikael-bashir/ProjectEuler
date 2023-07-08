from datetime import datetime
initial = datetime.now()


def CountWays(n):

    table = [0] * (n + 1)

    table[0] = 1

    for i in range(1, n):

        for j in range(i, n + 1):
            table[j] += table[j - i]

    return table[n]


# driver program
def main():
    for i in range(2, 10**2021):
        temp = CountWays(i)
        if pow(temp, 1, 1000000) == 0:
            break
    print()
    print(i)


if __name__ == '__main__':
    main()


run_time = datetime.now() - initial
print(run_time)

