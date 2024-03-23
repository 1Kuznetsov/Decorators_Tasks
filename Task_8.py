import logging
from datetime import datetime


def log_exceptions(log_file):
    logging.basicConfig(filename=log_file, level=logging.ERROR)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except Exception as exc:
                logging.error(f"{datetime.now()} - {type(exc).__name__}: {str(exc)}")
        return wrapper
    return decorator


@log_exceptions("exceptions_divide.log")
def divide(x, y):
    return x / y


print(divide(21, 0))
