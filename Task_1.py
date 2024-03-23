def count_upper(ptr, i, j):
    return len(list(filter(lambda x: x.isupper(), ptr[i-1:j])))
