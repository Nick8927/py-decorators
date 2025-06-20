import functools
import time


def cache_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Кеширует результаты вызовов функции для одинаковых аргументов /
        Caches the results of function calls for the same arguments.
        """
        key = args
        if kwargs:
            key += tuple(sorted(kwargs.items()))

        if key in wrapper._cache:
            print(f"Returning cached result for args={args}, kwargs={kwargs}")
            return wrapper._cache[key]

        result = func(*args, **kwargs)
        wrapper._cache[key] = result
        return result

    wrapper._cache = {}
    return wrapper


@cache_result
def slow_multiply(a, b):
    print(f"Computing {a} * {b}...")
    time.sleep(2)
    return a * b


print(slow_multiply(3, 5))
print(slow_multiply(3, 5))
print(slow_multiply(2, b=4))
print(slow_multiply(2, b=4))
