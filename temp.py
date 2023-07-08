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


#------------------------------------

perm_list = []
num_list = []

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

#----------------------------------------------
# useful functions:
#---------------------------------------------

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

#------------------------------------------------

if i/j == int(str(j)[1])/int(str(i)[1]):


#-----------

# square check: if (i**(1/2)) == (i**(1/2))//1:

#-----------------------

# code to find e by brute forcing all possible a, b, c, d, combinations and combinations of 6 and 0 in 6
# digits (in big c_list)
# this code also gives us the value of a, as for all working combinations of a, b, c, d, a is the same.
for values in big_c_list:
    for a in possible_abcd:
        for b in possible_abcd:
            for c in possible_abcd:
                for d in possible_abcd:
                    product = 1
                    product = a * a * b * c * d
                    for k in k_list:
                        if int(product * k) == int(values):
                            possible_e.append(k)
                            print(k, a, b, c, d, values)


a_check = '''

# code to find e by brute forcing all possible a, b, c, d, combinations and combinations of 6 and 0 in 6
# digits (in big c_list)
# this code also gives us the value of a, as for all working combinations of a, b, c, d, a is the same.
for values in big_c_list:
    for a in possible_abcd:
        for b in possible_abcd:
            for c in possible_abcd:
                for d in possible_abcd:
                    product = 1
                    product = a * a * b * c * d
                    for k in k_list:
                        if int(product * k) == int(values):
                            possible_e.append(k)
                            print(k, a, b, c, d, values)
                            
'''

----------------------------------

def is_pal(n):
    n = str(n)
    length = len(n)
    count = 0
    if length%2 == 0:
        for i in range(0, int(length/2)):
            if n[i] == n[-i-1]:
                count += 1
        if count == int(length/2):
            return 1
    elif length == 1:
        return 1
    else:
        for i in range(0, int(length//2)):
            if n[i] == n[-i-1]:
                count += 1
        if count == int(length//2):
            return 1


def reverse(n):
    n = str(n)
    revert = ''
    for i in range(0, len(n)):
        revert += n[-1-i]
    return int(revert)

----------------------------------

class FSM:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state = 0):
        name = name.upper()
        self.handlers.update({name: handler})
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise ValueError('must set start state before running')
        if not self.endStates:
            raise ValueError('must set at least one end state before running')
        iterator = 0
        answer = []
        while True: # consider switching for 'for i in range(1, 'inf')'
            newState, cargo, iterator, answer = handler(cargo, iterator, answer)
            iterator += 1
            if newState.upper() in self.endStates:
                # can add end states here
                print(answer)
                print('finished!')
                break
            else:
                handler = self.handlers[newState.upper()]


------------------------

anagram

import itertools
import datetime
import bisect

'''

anagram = str(input('enter anagram: '))
word = str(input('enter the word'))

'''

anagram = 'ab'
word = 'abxabaghabdgsahfuddahfbaab'


initial_time = datetime.datetime.now()


unique = {}
a_list = []
start_l = []


for a in anagram:
    a_list.append(a)


perms = list(itertools.permutations(a_list))
for i in perms:
    ana = list(i)
    temp = ''
    for a in ana:
        temp += a
    unique.update({temp: 1})


for anagr in unique:
    if len(anagr) < len(word):
        for i in range(0, (len(word)-len(anagr)+1)):
            count = 0
            for j in range(0, len(anagr)):
                if word[i+j] == anagr[j]:
                    count += 1
            if count == len(anagr):
                bisect.insort(start_l, i)
print(start_l)


run_time = datetime.datetime.now() - initial_time

print('\n', run_time)

time = 00.000130

ans = [0, 3, 4, 8, 22, 24]

-----------------------------------

from copy import copy
from datetime import datetime

initial = datetime.now()


def stairs(n, steps):
    paths = {0: 1, n: 0}

    # don't loop if only n is left in dict
    finished = True
    for i in paths:
        if i != n:
            finished = False
            break

    while not finished:
        new_paths = {n: paths[n]}

        for p, c in paths.items():
            for s in steps:
                if p + s <= n:
                    if (p + s) in new_paths:
                        new_paths[p + s] += c
                    else:
                        new_paths[p + s] = c

        # don't loop if only n is left in dict
        finished = True
        for i in paths:
            if i != n:
                finished = False
                break

        paths = copy(new_paths)

    return paths[n]


print(stairs(1000, [1, 3, 5]))
run_time = datetime.now() - initial
print(run_time)

------------------------

# Note - I am assuming we are not implementing a circular linked list, please let me know if that is wrong. I have looked
# at your comments and redone my code. Also, I am appending data at the tail, and removing data at the head.

# Max size of list


MAX_SIZE = 10

# Pointers

first_pointer = 0
is_pointing_at = '->'
head_pointer = -1
tail_pointer = -1
heap_pointer = first_pointer

# Data structure for linked list

data = []
free = []
free_ptr = []
data_ptr = []

# create and initialise list

for i in range(1, MAX_SIZE + 1):
    free.append(None)
    free_ptr.append(i)

# the last ptr is pointing at nothing

ptr[-1] = -1
print(ptr)

def format_space(num):
    space = ''
    for i in range(num):
        space += ' '
    return space


def free_dump():
    if 0 == heap_pointer:
        print(format_space(len('head_pointer -> ') - 6), 'heap,', first_pointer, is_pointing_at, free[0], is_pointing_at, ptr[first_pointer])
    else:
        print(format_space(len('head_pointer -> ')), 0, is_pointing_at, free[0], is_pointing_at, ptr[0])
    for j in ptr[:-1]:
        if j == heap_pointer:
            print(format_space(len('head_pointer -> ') - 6), 'heap,', j, is_pointing_at, free[j], is_pointing_at, ptr[j])
        else:
            print(format_space(len('head_pointer -> ')), j, is_pointing_at, free[j], is_pointing_at, ptr[j])

free_dump()


def list_dump()
    for j in range(0, len(data)):
        if j == head_pointer and tail_pointer:
            print(format_space(len('head_pointer -> ') - 11), 'head, tail', j, is_pointing_at, data[j], is_pointing_at, j + 1)
        elif j == head_pointer:
            print(format_space(len('head_pointer -> ') - 6), 'head,', j, is_pointing_at, data[j], is_pointing_at, j + 1)
        elif j == tail_pointer:
            print(format_space(len('head_pointer -> ') - 6), 'tail,', j, is_pointing_at, data[j], is_pointing_at, j + 1)


# append data (at the end)


def append_data(dt):
    global heap_pointer, head_pointer, tail_pointer, data, ptr
    if heap_pointer != -1:
        if tail_pointer == -1:  # and head_pointer == tail_pointer, check if empty
            data[heap_pointer] = dt
            last_heap = heap_pointer
            heap_pointer = ptr[heap_pointer]
            head_pointer, tail_pointer = last_heap, last_heap
        else:
            data[heap_pointer] = dt
            last_heap = heap_pointer
            heap_pointer = ptr[heap_pointer]
            tail_pointer = last_heap
    else:
        raise IndexError("there isn't enough space!")



# remove data (at the start)


def remove_data():
    global head_pointer, tail_pointer, heap_pointer, data, ptr
    if head_pointer == -1:  # and head_pointer == tail_pointer, check if empty
        raise IndexError('list is empty!')
    else:
        data[head_pointer] = '_'  # None
        if head_pointer == tail_pointer:  # check to see if the deleted data was the only data in list
            head_pointer, tail_pointer = -1, -1  # not circular list, and list is empty, so now they must be -1
        else:
            head_pointer = ptr[head_pointer]  # next head
        #if tail_pointer == -1:
        #   heap_pointer = 0


------------------

#golbach conjecture

from datetime import datetime
from sympy import isprime
from random import randrange

initial = datetime.now()
demo = 4482359328
dummy = 12
number = 4 * (10**18)

test = {}
test_l = []


for n in range(1, 100000):
    test.update({randrange(2, (9*(10**1300))+1, 2): 1})


for i in test:
    test_l.append(i)


def is_gold(num):
    upper = int(num//2)
    result = 0
    for i in range(2, upper+1):
        if isprime(i) and isprime(num-i):
            result = 1
            break
    return result


for i in test_l:
    print(i)
    if not is_gold(i):
        print(i, 'breakthrough!')
        break


run_time = datetime.now() - initial
print(run_time)

-----------------------------

one_two_l = 'string'

'''

phi_pos = (1 + (5**0.5))/2
phi_neg = (1 - (5**0.5))/2


def nth_stair(N):
    N = N+1
    answer = round(((phi_pos**N) - (phi_neg**N))/(5**0.5))
    return answer
test = nth_stair(1000)
print(test)

'''

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def multiplicativeInverse(a, n):
    s, t, nextS, nextT = n, 0, a, 1

    while nextS:
        wholeDiv = s // nextS
        t, nextT = nextT, t - wholeDiv * nextT
        s, nextS = nextS, s - wholeDiv * nextS

    if s > 1:
        print('a does not have a multiplicative inverse')
    if t < 0:
        t = t + n
    return t

print(multiplicativeInverse(7, 15))

charToCode = {' ': 32, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75,
                 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86,
                 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}

codeToChar = {32: ' ', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K',
                 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V',
                 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}

print(wrap(message, 2))








-------------------------------------------------------


from datetime import datetime

one_two_l = 'string'

'''

phi_pos = (1 + (5**0.5))/2
phi_neg = (1 - (5**0.5))/2


def nth_stair(N):
    N = N+1
    answer = round(((phi_pos**N) - (phi_neg**N))/(5**0.5))
    return answer
test = nth_stair(1000)
print(test)

'''

initial = datetime.now()

X = []
for i in range(1, 5):
    X.append(i)
print(X)
X.sort()


def ways(N, X):
    maxi = X[-1]
    least = 0
    last = {0: 1}  # a dictionary of N: number of ways, beginning with N = 0
    for n in range(1, N + 1):
        num_ways = 0
        for j in X:
            if n >= j:
                num_ways += last.get(n - j)
            else:
                break
        if len(last) < maxi:
            last.update({n: num_ways})
        else:
            del last[least]
            least += 1
            last.update({n: num_ways})

    result = last.get(least + maxi - 1)  # result is the value corresponding to the last key in last
    # problem with this, need to fix
    return result


answer = ways(5, X)

run_time = datetime.now() - initial

print(answer)
print()
print(run_time)


power = 1
    while power < n:
        power *= s
    return n == power

if (last(n) % 2) != (last(s) % 2):
    return False




def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def reduce(a, b, c):
    divisor = gcd(gcd(a, b), c)
    return int(a/divisor), int(b/divisor), int(c/divisor)


--------------------

from datetime import datetime
from math import ceil, sqrt

start = datetime.now()


def EratosthenesSieve(N: int) -> list:
    '''
    Calculating SPF (Smallest Prime Factor) for every number till N.
    Time Complexity : O(NloglogN)
    '''
    N += 1
    # stores smallest prime factor for every number
    spf = [*range(N)]

    # separately marking spf for every even number as 2
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, ceil(sqrt(N))):
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers divisible by i
            for j in range(i * i, N, i):
                # marking spf[j] if it is not previously marked
                if (spf[j] == j):
                    spf[j] = i
    return spf



def getReducedFactorization(N:int, spf:list)-> int:
    """
    counts repetition of each prime from prime factorisation of N
    using trial method upon spf list, and calculating the ceil of
    half of all prime's powers (pow(p, ceil(a / 2))) and multiplying
    them together.
    """
    gamma = 1
    while (N != 1):
        # keep a prime in prev variable
        prev = spf[N]
        # for counting the power
        c = 0
        # counts power of a prime
        while spf[N] == prev:
            c += 1
            N //= spf[N]
        # multiplies the half ceil of power on primes
        gamma *= pow(prev, ceil(c / 2))
        prev = spf[N]
    return gamma


def pythagoreanTriplets(n):
    # calculate spf array
    lengths = {}
    spf = EratosthenesSieve(2 * (n - int(sqrt(2 * n - 1))))

    # looping for every values of 2*b
    for b2 in range(4, 2 * (n - int(sqrt(2 * n - 1))), 2):

        # calculates reduced factor of 2*b
        gamma = getReducedFactorization(b2, spf)

        # for finding all triplets from 2*b
        for i in range(1, int(sqrt(b2 * ((b2 // 2) - 1))) // gamma + 1):
            i *= gamma
            sqVal = i * i
            q = sqVal // b2
            if q + i + (b2 // 2) > n:
                break
            else:
                x = q + i
                total = x + (b2 // 2) + i + x + (b2 // 2)
                if total <= 1_500_000:
                    print(x, (b2 // 2) + i, x + (b2 // 2))
                    lengths.update({x + (b2 // 2) + i + x + (b2 // 2): 1})
    return len(lengths)


print(pythagoreanTriplets(1_500_000))


runTime = datetime.now() - start

print()
print('run time:', runTime)
print()


--------------

5 5 6
17 17 16
65 65 66
241 241 240
901 901 902
3361 3361 3360
12545 12545 12546
46817 46817 46816
174725 174725 174726
652081 652081 652080
2433601 2433601 2433602
9082321 9082321 9082320
33895685 33895685 33895686
92604733 92604733 92604734
126500417 126500417 126500416
185209465 185209465 185209464
194291787 194291787 194291788
253000835 253000835 253000836
286896519 286896519 286896518
311709883 311709883 311709884
329874525 329874525 329874524
5479171588


------------

211
1231
2341
3331
5671
10201
11311
13321
14431
14641
15661
16771
17761
20101
24631
25741
27751
28861
29071
30091
31201
32191
34531
39061
40171
42181

--------


possible = True
                compare = pow(remainderL[0], 1, gcd)
                for i in range(1, lengthR):
                    if compare != pow(remainderL[i], 1, gcd):
                        possible = False
                if possible:
                    for i in range(1, lengthR):  # no need to change 1st congruence, as still all co-prime
                        modulusL[i] = int(modulusL[i] / gcd)
                        remainderL[i] = pow(remainderL[i], 1, modulusL[i])
                    return chineseRemainder(remainderL, modulusL)
                else:
                    return -1, -1

def reflectionsToLevel(n):  # takes in the number of reflections
    return int((n+3)/2)


def startingVertex(n):  # takes in the level number, returns middle or middle-right vertex
    lastDigit = int(str(n)[-1])
    return ['A', 'B'][lastDigit % 2], (lastDigit % 2)


def isValidVertex(coordinate):  # takes in a tuple of coordinates
    if gcd(coordinate[0], coordinate[1]) == 1:
        return True
    else:
        return False


def numOfEvensBetween(a, b):  # inclusive
    return int(b/2) - int((a-1)/2)


def driver(reflections):  # quite hard to make a general function, not complete
    level = reflectionsToLevel(reflections)
    lastVertex = int((level+1)/2)-1
    start, index = startingVertex(level)
    currentVertex = start
    numWays = 0
    vertices = ['A', 'B', 'C']
    if start == 'A':
        step = 2
    else:
        step = 1
    print(index, start, lastVertex)
    print()
    for i in range(1, lastVertex+1):
        if currentVertex == 'C':
            print(i*step, level)
            if isValidVertex((i*step, level)):
                numWays += 1
        index += 1
        currentVertex = vertices[index % 3]

    print()
    return 2*numWays


def solution(reflections):
    level = reflectionsToLevel(reflections)
    lastVertex = int((level + 1) / 2) - 1
    start, index = startingVertex(level)
    currentVertex = start
    numWays = 0
    vertices = ['A', 'B', 'C']
    print(start, lastVertex)
    if start == 'A':
        step = 2
    else:
        step = 1
    for i in range(1, lastVertex + 1):
        if currentVertex == 'C':
            numWays+=1
        index += 1
        currentVertex = vertices[index % 3]
    return 2 * numWays


if pivot == 0:
    for j in range(length):
        matrix[j] = matrix[j][1:]
        return gausianElimination(matrix)



'''

from datetime import datetime
from sympy.ntheory import factorint
from sympy.ntheory.modular import crt
from sympy import primefactors
import random
from modular import generalChineseRemainder, totient
import modular


initial = datetime.now()


def reducer(expression):
    notInt = ['[', ']', ',', ' ', '']
    reduced = False
    while not reduced:
        print("".join(expression))
        nestCounter = 0
        leftNum, rightNum = None, None
        restart = True
        tooBig = None
        explodingPairIndex = None
        length = len(expression)
        for i in range(length):
            if expression[i] == '[':
                nestCounter += 1
            if expression[i] == ']':
                nestCounter -= 1
            if nestCounter == 4:
                explodingPair = ''
                explodingPairIndex = [i, i]
                for j in range(i+2, length):
                    if expression[j] == ']':
                        explodingPairIndex[1] = j
                        break
                    else:
                        explodingPair += str(expression[j])
                explodingPair = explodingPair.replace(',', '')
                index = i
                break
            if expression[i] not in notInt:
                if restart:
                    leftNum = [i, i]
                    restart = False
                else:
                    leftNum[1] += 1
            elif expression[i] in notInt:
                restart = True
        if explodingPairIndex != None:
            if leftNum != None:
                temp = int(''.join(expression[leftNum[0]:leftNum[1]+1]))
                expression = list(expression[0: leftNum[0]]) + list(str(temp + int(explodingPair[0]))) + list(expression[leftNum[1]+1: length])
            found = False
            for i in range(length):
                if (expression[i] not in notInt) and (not found):
                    rightNum = [i, i]
                    found = True
                elif found:
                    rightNum[1] = i
                break
            if rightNum != None:
                temp = int(''.join(expression[rightNum[0]:rightNum[1]+1]))
                expression = list(expression[0: rightNum[0]]) + list(str(temp + int(explodingPair[1]))) + list(expression[rightNum[1]+1: length])
            expression = list(expression[0: explodingPairIndex[0]]) + ['0'] + list(expression[explodingPairIndex[1]+1: length])
        elif explodingPairIndex == None:
            reduced = True
    return ''.join(expression)



print(reducer('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'))


def adder(pair):
    return [pair[0]] + [pair[1]]



runTime = datetime.now() - initial



second = datetime.now()


secondTime = datetime.now() - second


print()
print(runTime)
print(secondTime)




'''

'''
#a)

from datetime import datetime
from collections import OrderedDict
from math import ceil, factorial
from itertools import combinations




first = datetime.now()


def ith(final, i):
    mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
               13: 'M', 14: 'N', 15: 'O', 16: 'P'}
    locations = {}
    distribution = []
    products = []
    for j in range(len(final)):
        locations[final[j]] = j
    time = []
    locations = OrderedDict(sorted(locations.items()))
    for j in range(len(final)):
        time.append(None)
    for j in locations:
        index = locations[j]
        area = [index]
        time[index] = j
        while index > 0:
            if time[index-1] == None:
                break
            index -= 1
        area.append(index)
        possibilities = []
        for k in range(area[1], area[0]+1):
            possibilities.append(mapping[k+1])
        distribution.append(possibilities)
    product = 1
    for j in distribution[::-1]:
        product *= len(j)
        products.append(product)
    products = products[::-1]
    result = ''
    if i > products[0]:
        i = products[0]
    for j in range(len(final)):
        length = len(distribution[j])
        branches = products[j]//length
        index = ceil(i/branches) - 1
        i -= index*branches
        result += distribution[j][index]
    return result


answer = ith('OPNMLKJIHGFEDCBA', 3)

firstTime = datetime.now() - first

print(answer)


print()
print(firstTime)
print()

#b)

'eeccggaaaa'
'GHCDABEFIJ'

#c)


if there was exactly one preference list, the arrangement could only be 'PONMLKJIHGFEDCBA'
so, if there are exactly two preference lists, arrangements could be 'OPNMLKJIHGFEDCBA', 'PNOMLKJIHGFEDCBA', ... ,
'PONMLKJIHGFEDCBA'


#d)


1st car (A) must be in it's preferred spot, because a car will only park in 1st spot if it prefers it (and it is empty).


comb = []
for i in range(1, 16):
    comb.append(i)
comb = list(combinations(comb, 2))
print(comb)
sum = 0
num = factorial(15)
for i in comb:
    sum += num // (i[0] * i[1])
print(sum)
'''

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k


def closedForm(n, m):
    if m >= n:
        return 0.5**n
    if m == 1:
        return 1/(n+1)
    answer = 0
    for i in range(1, n-m+1):
        answer += g(m-2, i)*(1/(closedForm(n-m+2-i, 1)))
    for i in range(m-1):
        answer += g(i, n-m)*(2**(m-i))
    return 1/answer

def closedForm(n, m):
    answer = 0
    for i in range(1, n-m+1):
        answer += g(m-2, i)*(n-m+3-i)
    for i in range(m-1):
        answer += g(i, n-m)*(2**(m-i))
    return 1/answer

def g(x, k):
    if x == 0:
        return 1
    if x == 1:
        return k
    if x == 2:
        return 0.5*k*(k+1)
    answer = 0
    for i in range(1, k+1):
        answer += g(x-1, i)
    return answer

def closedForm(n, m):
    answer = 0
    for i in range(1, n-m+1):
        answer += g(m-2, i)*(n-m+3-i)
    for i in range(m-1):
        answer += g(i, n-m)*(2**(m-i))
    return 1/answer