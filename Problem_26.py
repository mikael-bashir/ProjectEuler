from functools import reduce
import sympy

def factors(n):
    f_list = []
    for i in set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))):
        f_list.append(i)
    f_list.remove(n)
    return f_list

def totient(n):
    totient = n
    f_list = factors(n)
    for i in f_list:
        if sympy.isprime(i):
            totient *= (i-1)/i
            totient = int(totient)
    if sympy.isprime(n):
        totient = n-1
    return totient

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def p_factors(n):
    p_f_list = []
    for i in factors(n):
        if sympy.isprime(i):
            p_f_list.append(i)
    if sympy.isprime(n):
        p_f_list.append(n)
    return p_f_list

maximum_i = 1
maximum_period = 0

for i in range(2, 1000):
    m = i
    while 2 in p_factors(m):
        m = int(m/2)
    while 5 in p_factors(m):
        m = int(m/5)
    if m != 1:
        totient_f = factors(totient(m))
        totient_f.append(totient(m))
        n = len(totient_f)
        quickSort(totient_f, 0, n - 1)
        for j in totient_f:
            if ((10 ** j) - 1) % m == 0:
                period = j
                break
        if period > maximum_period:
            maximum_i = i
            maximum_period = period
    elif m == 1:
        string = 'pass'

print(maximum_i, maximum_period)