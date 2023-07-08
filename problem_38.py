def pan_check(n):
    p_list = []
    check = 0
    count = 0
    for i in str(n):
        p_list.append(int(i))
    p_list.sort()
    if p_list[0] == 1 and len(p_list) == 9:
        for j in range(0, len(p_list)-1):
            if p_list[j]+1 == p_list[j+1]:
                count += 1
        if count == len(p_list)-1:
            check = 1
    return check


def prodsum(n, l):
    summation = ''
    for i in l:
        summation += str(n*int(i))
    return summation


max_pan = 0
for i in range(1, 10001):
    for j in range(2, 10):
        initial = 1
        m_list = [initial]
        while m_list[-1] != j:
            initial += 1
            m_list.append(initial)
        concat = prodsum(i, m_list)
        if pan_check(concat):
            if int(concat) > max_pan:
                max_pan = int(concat)
                print(i, m_list)


print(max_pan)


