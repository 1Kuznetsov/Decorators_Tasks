import functools
import math


def is_root(n):
    a = int(math.sqrt(n))
    return a * a == n


def multiply_nums(a, b, c):
    return functools.reduce(lambda x, y: x*y, [i for i in range(a, b+1) if i % c == 0 and is_root(i)])
