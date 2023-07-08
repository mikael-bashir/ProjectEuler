my_list = []
for i in range(2, 354296):
    f_p_sum = 0
    for j in str(i):
        f_p_sum += (int(j))**5
    if i == f_p_sum:
        my_list.append(i)


answer = 0
for i in my_list:
    answer += int(i)

print(answer)




