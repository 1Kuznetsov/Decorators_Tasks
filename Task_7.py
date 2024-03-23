import json


def to_json_format(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper


@to_json_format
def squares(k):
    lst = []
    for j in range(k):
        lst.append(j ** 2)
    return lst


@to_json_format
def diff_symbols(ptr):
    d = {}
    for item in ptr:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d


@to_json_format
def get_data(count):
    lst = []
    for _ in range(count):
        lst.append(input())
    return {'data': lst}


print(squares(int(input())))
print(diff_symbols(input()))
print(get_data(int(input())))
