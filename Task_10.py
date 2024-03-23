from time import time


def restriction(time_limit, call_limit):
    def decorator(func):
        calls = 0
        start_time = time()

        def wrapper(*args, **kwargs):
            nonlocal calls
            time_passed = time() - start_time

            if time_passed > time_limit:
                raise TimeoutError('Exceeded time')
            calls += 1

            if calls > call_limit:
                raise RuntimeError('Exceeded amount of calls')

            return func(*args, **kwargs)

        return wrapper
    return decorator


@restriction(0.001, 5000)
def test():
    print("Hello, world!")


try:
    for i in range(10000):
        test()
except TimeoutError as exc:
    print(f"TimeoutError: {exc}")
except RuntimeError as exc:
    print(f"RuntimeError: {exc}")
