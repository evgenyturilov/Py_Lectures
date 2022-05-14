def f(x):
    return x**2

g = f
print(type(f))
print(type(g))


def calc_1(x):
    return x + 10

print(calc_1(10))

def calc_2(x):
    return x*10

print(calc_2(10))

def math(op, x):
    print(op(x))

math(calc_2, 10)
math(calc_1, 10)

def sum(x, y):
    return x + y

f = sum
summ = lambda x, y: x + y + 1

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    # return(op(a, b))

calc(mult, 4, 6)
calc(summ, 3, 6)
calc(lambda x, y: x + y, 4, 7)