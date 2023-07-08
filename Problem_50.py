from sympy import primerange
from sympy import isprime
from datetime import datetime

now = datetime.now()

upper = 1001

p_list = list(primerange(upper))

length = len(p_list)
chain_sum = 0
greatest_chain = 0
outer_flag = False # we have found the greatest length chain
inner_flag = False # we move on to the next smallest window, as a window has been found to exceed sum upper - 1, hence
# all other windows will exceed upper - 1

for i in range(1, length-1):
    if outer_flag:
        break
    window_size = length - i
    inner_flag = False
    for j in range(0, i+1):
        if not inner_flag:
            chain_sum = 0
            window = p_list[j:window_size+j]
            for primes in window:
                chain_sum += primes
            if chain_sum < (upper-1):
                if isprime(chain_sum):
                    outer_flag = True
                    inner_flag = True
                    greatest_chain = chain_sum
            else:
                inner_flag = True

print(greatest_chain)

run_time = datetime.now() - now

print(run_time)

997651
time = '''
0:05:50.450702
'''

41
time1 = '''
0:00:00.000338
'''

953
time2 = '''
0:00:00.002244
'''
