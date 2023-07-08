from math import sin


def discreteUniformOscillator(n):  # returns a sign depending on the parity of a natural n
    return (-1)**n


def continuousUniformOscillator(n):  # sin / mod sin
    pass


def continuousCompoundOscillator(n, f):
    pass


def sign(r):  # returns the sign of a non-zero real r
    return r/modulus(r)


def nullifier(r):  # returns 0 if a non-zero real r is positive, 1 if negative
    return (modulus(r)-r)/(-2*r)
    pass


def modulus(r):  # returns the modulus of a real r
    return (r**2)**(1/2)


def max(a, b):
    return (a+b+(sign(a-b)*(a-b)))/2


def min(a, b):
    return (a+b+(sign(b-a)*(a-b)))/2


def ceiling(r):
    pass


def floor(r):
    pass


# ---------------------------------------------
#
# ---------------------------------------------

def function(x):
    pass

def limitToInf(speed=3, limit=1000):
    last = 0
    current = 1
    n = 10**speed
    increment = 10**speed
    count = 0
    while (current != last) and (count < limit):
        last = current
        current = function(n)
        n += increment
        count += 1
    return current
