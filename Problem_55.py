

def is_pal(n):
    n = str(n)
    length = len(n)
    count = 0
    if length%2 == 0:
        for i in range(0, int(length/2)):
            if n[i] == n[-i-1]:
                count += 1
        if count == int(length/2):
            return 1
    elif length == 1:
        return 1
    else:
        for i in range(0, int(length//2)):
            if n[i] == n[-i-1]:
                count += 1
        if count == int(length//2):
            return 1


def reverse(n):
    n = str(n)
    revert = ''
    for i in range(0, len(n)):
        revert += n[-1-i]
    return int(revert)


l_count = 0


for i in range(1, 10001):
    flag = 0
    num = i
    for j in range(1, 51):
        num = num + reverse(num)
        if is_pal(num):
            flag = 1
            break
    if not flag:
        l_count += 1


print(l_count)



