# instead of finding all numbers which CANNOT be written as abundant sums, this solution negates
# the negation of the task, that is it finds -(the sum of all numbers which CAN be written as abundant
# sums) + (the sum of all numbers smaller or equal to the maximum number which CAN be written as abundant sums)


# Note: current estimated RunTime: < 20s


def d(n): # defining an aliquot sum function to find if n is abundant or not
    p_div_sum = 0
    root = int(((int(n))**(1/2))//1)
    n = int(n)
    for i in range(1, root+1):
        if n % i == 0:
            p_div_sum += i + int(n/i)
    if int(n) == 1:
        p_div_sum = 0
    elif ((int((n**(1/2))//1))**2) == n:
        p_div_sum = p_div_sum - int((n**(1/2))//1)
    if int(n) != 1:
        p_div_sum += -n
    return p_div_sum


abundant_list = []  # to append numbers which are abundant (less than 28124)
running_sum = 0  # to add up all the numbers which CAN be written as abundant sums
num_list = []  # to append the natural numbers below 28124
num_to_add = {}  # a dictionary of numbers to add, whose primary goal is to check if key entries are unique rather than
# storing
maxim = 0  # initialising maxim to the smallest possible key in num_to_add, in order to find maximum in dict


for i in range(1, 28124):
    if d(i) > i:
        abundant_list.append(i)
    num_list.append(i)


for i in abundant_list:
    for j in abundant_list:
        if i+j < len(num_list):
            if num_list[i+j-1] == i+j:
                try:
                    test = num_to_add.get(i+j) + 1
                except TypeError:
                    num_to_add.update({i+j: 1})


for i in num_to_add:
    if i > maxim:
        maxim = i
    running_sum += i


print(int((maxim*(maxim+1))/2) - running_sum)  # finally prints the negation of the negation of the task

