def resulter(func):
    def wrapper(x):
        result = func(x)
        print(result)
        return result
    return wrapper


@resulter
def cube(num):
    return num ** 3
