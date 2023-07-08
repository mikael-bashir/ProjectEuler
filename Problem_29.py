num_list = []
num_dict = {}


for a in range(2, 101):
    for b in range(2, 101):
        num_list.append(a**b)


num_list.sort()

for i in num_list:
    num_dict.update({i: 1})

print(len(num_dict))