import sympy

def truncate(n):
    trunc = str(n)
    trunk = str(n)
    t_list = [int(n)]
    count = 0
    while len(str(trunc)) > 1:
        count += 1
        trunk = str(n)[:-count]
        trunc = str(n)[count:]
        t_list.append(int(trunc))
        t_list.append(int(trunk))
    return t_list

p_found = 0
n = 0
ans_list = []
answer = 0

while p_found < 15: #  accounting for the 4 one digit primes
    n_list = truncate(n)
    count = 0
    for i in n_list:
        if sympy.isprime(int(i)):
            count += 1
    if count == len(n_list):
        p_found += 1
        if n not in [2, 3, 5, 7]:
            ans_list.append(n)
    n += 1

for i in ans_list:
    answer += i

print(answer)

