fibonacci_list = [1, 1]
counter = 2


while len(str(fibonacci_list[-1])) < 1000:
    fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
    counter += 1

print(counter)
