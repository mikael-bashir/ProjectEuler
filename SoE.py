import mpmath
from mpmath import *
import numpy as np
from datetime import datetime


start = datetime.now()


def gausianElimination(matrix):  # in progress
    length = len(matrix)
    for i in range(length+1):
        pivot = None
        for j in range(length):
            if matrix[j][i] != 0:
                pivot = j
                break
        if pivot != None:
            matrix[i][i], matrix[i][pivot] = matrix[i][pivot], matrix[i][i]


def solveSystem(system, constants):
    solution = np.linalg.inv(system).dot(constants)
    return solution



print(solveSystem([[1, 3, 2, 4, 2, 432], [4, 3, 2, 43, 2, 342], [45, 7645, 65, 2, 65, 4], [56, 346, 2, 5654, 6, 4],\
                  [55, 35, 6323, 65324, 65, 534], [6542, 567, 3, 24, 342, 543]], [43, 14512453, 6, 435, 6, 765]))


print(10**(-7))


print(datetime.now() - start)