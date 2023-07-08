import sympy
import math


def quad(c):
    a = 1
    b = 1
    c = -(2*c)
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    if sol1 == sol1 // 1:
        return 1
    elif sol2 == sol2 // 1:
        return 1
    else:
        return 0


with open('words.txt', 'r') as words:
    for line in words:
        line = line.replace('\n', '')
        line = line.replace('"', '')
        w_list = line.split(',')


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
a_to_n = {}
counter = 1
for i in alpha:
    a_to_n.update({i.upper(): counter})
    counter += 1


triangle_words = []
for i in w_list:
    score = 0
    for j in i:
        score += a_to_n.get(j)
    if quad(score):
        triangle_words.append(i)
print(len(triangle_words))