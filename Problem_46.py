import sympy

check = False
for i in range(2, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    i = (2*i)-1
    if not sympy.isprime(i):
        count = 0
        p_list = list(sympy.primerange(1, i))
        for j in p_list:
            if (((i-j)/2) ** (1 / 2)) != (((i-j)/2) ** (1 / 2)) // 1:
                count += 1
        if count == len(p_list):
            print(i)
            check = True
    if check:
        break





