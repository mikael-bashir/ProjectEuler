import itertools


perm_list = []
num_list = []
counter = 0


perm_list = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


for i in perm_list:
    number = ''
    for j in i:
        j = str(j)
        number += j
    num_list.append(number)


print(num_list[999999])

