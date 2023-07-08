f_part = ''
for i in range(1, 200000): # adjusted upper bound by trial and error, by printing length of f_part
    f_part += str(i)


answer = 1
for i in range(0, 7):
    answer *= int(f_part[(10**i)-1])


print(answer)
