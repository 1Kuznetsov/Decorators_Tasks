def count_spec_end_num(a, b, c, d):
    return sum(list(map(lambda x: x % c != 0 and x % 10 == d, range(a, b + 1))))
