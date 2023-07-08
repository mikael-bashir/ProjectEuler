def palindrome(n):
    check = 0
    n = str(n)
    if len(n)%2 == 0:
        count = 0
        for i in range(0, int(len(n)/2)):
            if n[i] == n[-i-1]:
                count += 1
        if count == int(len(n)/2):
            check = 1
    elif len(n)%2 == 1:
        count = 0
        for i in range(0, int((len(n)-1)/2)):
            if n[i] == n[-i - 1]:
                count += 1
        if count == int((len(n)-1)/2):
            check = 1
    return check


answer = 0
for i in range(1, 1000001):
    if palindrome(i) and palindrome(format(i, 'b')):
        answer += i


print(answer)

