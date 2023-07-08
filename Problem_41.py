import sympy
import itertools


def pan(n):
    check = 0
    str_l = []
    for i in str(n):
        str_l.append(int(i))
    str_l.sort()
    if str_l[0] == 1:
        count = 0
        for i in range(0, len(str_l)-1):
            if str_l[i]+1 == str_l[i+1]:
                count += 1
        if count == len(str_l)-1:
            check = 1
    return check


perms = []
for i in range(1, 10):
    m_list = []
    for j in range(1, i+1):
        m_list.append(j)
    p_list = list(itertools.permutations(m_list))
    for j in p_list:
        number = ''
        for k in j:
            number += str(k)
        perms.append(number)


max_pan_p = 0
for i in perms:
    if str(i)[-1] != 5:
        if int(i) % 2 != 0:
            if sympy.isprime(int(i)):
                if int(i) > max_pan_p:
                    max_pan_p = int(i)


print(max_pan_p)


