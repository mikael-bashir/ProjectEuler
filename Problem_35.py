import sympy
answer = 0

def rotations(n):
    count = 0
    upper = len(str(n))
    r_list = []
    n = str(n)
    if n == '1':
        r_list = [1]
    else:
        while count != upper:
            add = n[0]
            n = n[-len(n)+1:]
            n += add
            r_list.append(int(n))
            count += 1
    return r_list


for i in range(1, 1000001):
    p_count = 0
    i_list = rotations(i)
    for j in i_list:
        if sympy.isprime(j):
            p_count += 1
    if p_count == len(i_list):
        answer += 1


print(answer+4)
