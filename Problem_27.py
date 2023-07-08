import sympy

max_chain = 0
max_a_b = [0, 0]


def quad(a, b, x):
    y = (x**2)+(a*x)+b
    return y


for a in range(-999, 1000):
    for b in range(-1000, 1001):
        chain = 0
        x = 0
        while sympy.isprime(quad(a, b, x)):
            chain += 1
            x += 1
        if chain > max_chain:
            max_chain = chain
            max_a_b = [a, b]

print(max_chain)
print(max_a_b)

