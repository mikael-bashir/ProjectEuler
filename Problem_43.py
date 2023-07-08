import itertools

my_l = list(itertools.permutations('0123456789'))
print(my_l)


def list_to_str(n):
    number = ''
    n = list(n)
    for i in n:
        number += str(i)
    return int(number)


p_list = [2, 3, 5, 7, 11, 13, 17]
for i in my_l:
    string = list_to_str(i)
    count = 0
    for j in range(1, 8):
        if (int(str(string)[j: j+3])) % (p_list[i-1]) == 0:
            count += 1
    if count == 7:
        print(i)






