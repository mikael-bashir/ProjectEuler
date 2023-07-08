from datetime import datetime
from sympy import randprime

initial = datetime.now()


def multiplicativeInverse(a, n):
    s, t, nextS, nextT = n, 0, a, 1

    while nextS:
        wholeDiv = s // nextS
        t, nextT = nextT, t - wholeDiv * nextT
        s, nextS = nextS, s - wholeDiv * nextS

    if s > 1:
        raise ValueError('a does not have a multiplicative inverse!')
    if t < 0:
        t = t + n
    return t


def generateKeys():
    p, q = randprime(10**90, 10**100), randprime(10**90, 10**100)
    e = randprime(10**80, 10**90)
    return p, q, e


def encrypt(e, n, m):  # e, n, message
    ciphertext = []
    for i in m:
        code = int(ord(i))
        ciphertext.append(pow(code, e, n))
    return ciphertext


def decrypt(d, n, c):  # private, n, cipher
    message = ''
    for i in c:
        char = chr(pow(i, d, n))
        message += char
    return message



def main():
    message = '''
    Today's workshop is about RSA encryption, an industry standard that
    is still used today. It utilises the fact that it is very difficult 
    to factorise very large numbers. One of it's weaknesses is that it
    relies on pseudorandom numbers to generate keys, which aren't really
    random, and, given the seed, could be predicted.
    '''
    p, q, e = generateKeys()
    n = p*q
    totientPQ = (p - 1) * (q - 1)
    private = multiplicativeInverse(e, totientPQ)
    cipher = encrypt(e, n, message)
    message = decrypt(private, n, cipher)
    print(cipher)
    print(message)

main()























run_time = datetime.now() - initial
print()
print()
print(run_time)






