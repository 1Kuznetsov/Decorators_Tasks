import json
import xmltodict
import yaml


def serialize(frmt=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if format == 'xml':
                convert_result = xmltodict.unparse(result)
            elif format == 'yaml':
                convert_result = yaml.dump(result)
            else:
                convert_result = json.dumps(result)
            return convert_result
        return wrapper
    return decorator


@serialize('xml')
def squares(k):
    lst = []
    for j in range(k):
        lst.append(j ** 2)
    return lst


@serialize('yaml')
def diff_symbols(ptr):
    d = {}
    for item in ptr:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d


@serialize('xml')
def get_data(count):
    lst = []
    for _ in range(count):
        lst.append(input())
    return {'data': lst}


@serialize()
def get_person_data():
    return {"name": "Alice", "age": 25, "city": "New York"}


@serialize('xml')
def get_car_data():
    return {"brand": "Toyota", "model": "Camry", "year": 2020}


@serialize('yaml')
def get_product_data():
    return {"name": "Laptop", "price": 1000, "brand": "Dell"}


print(squares(int(input())))
print(diff_symbols(input()))
print(get_data(int(input())))
print(get_person_data())
print(get_car_data())
print(get_product_data())
