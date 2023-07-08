
# print(138901917 ** 2)

def check(n):
    n = str(n)
    result = True
    for i in range(1, 10):
        if n[2*i - 2] != str(i):
            result = False
            break
    return result


for i in range(105892122, 138902663):
    if check(i**2):
        print(i * 10)

