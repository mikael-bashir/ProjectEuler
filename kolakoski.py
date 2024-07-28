from datetime import datetime
from sympy import *
from sympy.ntheory import factorint
from math import factorial, pi
from numpy import sqrt
import modular
from collections import Counter

initial = datetime.now()




def kolakoski(n):
    if n==0:
        return None
    if n==1:
        return "1"
    if n<0:
        raise ValueError("negative value n passed to kolakoski")
    if type(n) != int:
        raise TypeError("non integer n passed to kolakoski")
    returnVal = "1"
    counter = 1
    parity = 0
    while True:
        for i in returnVal:
            parity = 1 - parity
            for j in range(int(i)):
                returnVal += str(1+parity)
                counter += 1
                if counter >= n:
                    break
            if counter >= n:
                break
        if counter >= n:
            break
    return returnVal







print(kolakoski(10))






first = datetime.now() - initial
print(first)

'''
...00110110100100110100101100100110110100110
...01010100001011110000101010100011110100100
...10110011110111010011100001100100001011000
...11010000101000100111101000110000100010000
-11101100110111011111101111100111111110
'''











