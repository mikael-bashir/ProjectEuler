import math
import sympy
import itertools

# since no number start with 0, a digit can only be 0 or not 0, and the only 5-digit number with equal digits, which
# has 4 distinct prime factors (a, b, c, d), is 66666. 1 across must be 66666, as each square is the start of a down
# number. Therefore, a, b, c, d, will be in the prime factorization of 66666
abcd_product = [66666]
# since we now know the only digits are 6 and 0, we can create two lists, one for across, one for down, for all
# the combinations of 6 and 0, in a five/six-digit number
c_list = [60000, 60006, 60060, 60066, 60600, 60606, 60660, 60666, 66000, 66006, 66060, 66066, 66600, 66606, 66660,
          66666]
big_c_list = [600000, 600006, 600060, 600066, 600600, 600606, 600660, 600666, 606000, 606006, 606060, 606066, 606600,
              606606, 606660, 606666, 660000, 660006, 660060, 660066, 660600, 660606, 660660, 660666, 666000, 666006,
              666060, 666066, 666600, 666606, 666660, 666666]
# this will be very useful in limiting our search space, as it is an efficient check to see if all elements of a list
# are unique, as keys must be unique
unique_check = {}


def primefactors(n):
    p_list = []
    while n % 2 == 0:
        p_list.append(2)
        n = n / 2

    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            p_list.append(i)
            n = n / i

    if n > 2:
        p_list.append(int(n))
    return p_list


for c in c_list:
    my_list = primefactors(c)
    for e in my_list:
        # using the check to create a list of prime factors that all variables in the puzzle MUST be in
        unique_check.update({e: 'x'})

# converting the dict into a useful list
primes = []
for i in unique_check:
    primes.append(i)

primes.sort()
unique_check = {}

allowed = ['6', '0']
list_of_abcd = []

# brute forcing to get a list of possible a, b, c, d
for a in primes:
    for b in primes:
        for c in primes:
            for d in primes:
                if (a * b * c * d) == 66666:
                    list_of_abcd.append([a, b, c, d])

# finding a simplified list of possible a, b, c, d
short_abcd = []
for i in list_of_abcd:
    i.sort()
    if i not in short_abcd:
        short_abcd.append(i)
# this is looking good - we have 4 elements, in which a, b, c, d must be.
possible_abcd = [2, 3, 41, 271]

# getting permutations of abcd list
abcd_perms = list(itertools.permutations(possible_abcd))
final_abcd = []
for i in abcd_perms:
    i = list(i)
    final_abcd.append(i)

# some simple calculations gives that e is limited to being at most 31250
possible_e = []
k_list = list(sympy.primerange(1, 31251))

# code to find e by brute forcing all possible a, b, c, d, and combinations of 6 and 0 in 6
# digits (in big c_list), by considering 4 down
e_check = ''' 'pass'

for c in big_c_list:
    for i in final_abcd:
        product = 1
        product = i[0] * i[0] * i[1] * i[2] * i[3]
        for k in k_list:
            if int(product * k) == int(c):
                possible_e.append(k)
                print(k, i, c)

'''

e = 5
a_check = ''' 'pass'

# code to find e by brute forcing all possible a, b, c, d, combinations and combinations of 6 and 0 in 6
# digits (in big c_list)
# this code also gives us the value of a, as for all working combinations of a, b, c, d, a is the same, by considering
# 4 down
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

a = 2
possible_f = []
b_check = ''' 'pass'

# this code gives us the value of b, as for each combination, b is the same, by considering 6 across, and also 
# 2 possible f
for values in c_list:
    if str(values)[3] == '6':
        for ax in possible_abcd:
            for bx in possible_abcd:
                for cx in possible_abcd:
                    for dx in possible_abcd:
                        product = 1
                        product = ax * ax * bx * bx * 5
                        if ax == 2:
                            for k in k_list:
                                if int(product * k) == int(values):
                                    possible_f.append(k)
                                    print(k, ax, bx, cx, dx, values)
                                    # upon analysing the values above that are printed, we can see that
                                    # f is in [337, 367], and that c, d are in [41, 271]. Further, all b and a are
                                    # 2, and 3, respectively, confirming that a is 2, and we find that b is 3.
                                    # Finally, notice that 'values' has got the same first and last 2 characters,
                                    # namely, the first character is 6, the last 2 is 60, always. So we can add this.
'''

# so far, we have:

a = 2
b = 3
possible_cd = [41, 271]
e = 5
possible_f = [337, 367]

# let us now consider 1 down
# 666666 / (2 x 3^2) = 37037


# print(primefactors(37037))
# interpreting the values given by the above implies that i,j,k,m, are in [7, 11, 13, 37]


possible_ijkm = [7, 11, 13, 37]

# now consider 10 across
j_check = ''' 'pass'

for i in possible_ijkm:
    for j in possible_ijkm:
        for k in possible_ijkm:
            for m in possible_ijkm:
                number = a * (b**2) * i * k * m
                if str(number)[0] == '6' and str(number)[3] == '0': # as these are the intersections
                    print(number, i, k, m)
                    # analysing the print gives that the only valid combinations of i, k, m are permutations of [7, 13,
                    # 37], implying that j is 11. Further, it is clear that the only possible value for 10 across is
                    # 60606

'''

j = 11
possible_ikm = [7, 13, 37]

# consider 9 across

l_check = ''' 'pass'

for values in c_list:
    product = (a**2) * b * e * j
    for k in k_list:
        if product * k == values:
            print(values, k)
            # after analysing the above print, we see that the only value l can take is 101
            # further, notice the only possible values satisfying our requirements is 66660, so we can add this to 
            # puzzle

'''

l = 101

# consider the possible values for ik:
ik_perm = []
for ix in possible_ikm:
    for kx in possible_ikm:
        if ix != kx:
            unique_check.update({ix * kx: 1})

for integers in unique_check:
    ik_perm.append(integers)

print(ik_perm)

# now we are ready to consider 2 down

m_check = ''' 'pass'

for ik in ik_perm:
    number = (a**2) * b * e * ik * (j**2)
    if str(number)[0] == '6' and str(number)[4] == '6' and str(number)[5] == '0':
        print(number, ik)
        # from analysing the above print, we have that 2 down is 660660, and reversing the ik = 91 gives that
        # i, k is in [7, 13], therefore m = 37

'''

m = 37
possible_ik = [7, 13]
# we know have 2 down, therefore we can now find f with 6 across
# scrolling up and doing the b_check gives: values must now be 66060, therefore the corresponding f must be 367
# we can add 66060 to the puzzle
# so far, we have:

a = 2
b = 3
possible_cd = [41, 271]
e = 5
f = 367
j = 11
l = 101
m = 37

# consider 7 across

across7 = ''' 'pass'

for values in c_list:
    number = values/(a*(b**2))
    if number == number//1:
        facts = primefactors(number)
        if len(facts) == 2:
            print(values, facts)
            # upon analysing the print, we see that the only possible value of values in 60066, as this is the only
            # that fits in our part-completed cross - so, g, h are in [47, 71]. We now add 60066 to cross.

'''

possible_gh = [47, 71]

# consider 8 across

across8 = ''' 'pass'

for values in c_list:
    if str(values)[0] == '6' and str(values)[1] == '6' and str(values)[3] == '6':
        for ik in ik_perm:
            number = a * b * (j**2) * ik
            if number == values:
                print(values, ik)
                # from the print, we have across 8 must be 66066, and once we add this, our cross puzzle is completed.

'''

# to conclude, we have:

a = 2
b = 3
cd = 11111
e = 5




