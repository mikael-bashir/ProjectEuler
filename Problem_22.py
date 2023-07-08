

alpha_to_num = {}
counter = 1
number_sum = 0
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


with open('input.txt', 'r') as file:
    for line in file:
        name_list = line.replace('"', '').split(',')
        name_list.sort()


for i in alpha:
    alpha_to_num.update({i.upper(): counter})
    counter += 1


for i in range(0, len(name_list)):
    temp = 0
    for j in name_list[i]:
        temp += alpha_to_num.get(j)
    number_sum += temp * (i+1)


print(number_sum)






