def nat_sum(a, b, c, d):
    return sum(list(filter(lambda x: x % c == 0 and x % d == 0, range(a, b + 1))))
