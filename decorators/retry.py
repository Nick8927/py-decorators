import time
import functools


def retry_decorator(times=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Повторяет вызов функции при исключении указанного типа до заданного количества раз с задержкой /
            Retries the function call on specified exceptions up to a given number of times with a delay.
            """
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(delay)
            raise Exception(f"Function '{func.__name__}' failed after {times} attempts.")

        return wrapper

    return decorator


import random


@retry_decorator(times=5, delay=2, exceptions=(ValueError,))
def unstable_operation():
    """Функция, которая с вероятностью 50% выбрасывает ValueError."""
    if random.random() < 0.5:
        print("Operation failed!")
        raise ValueError("Random failure occurred")
    print("Operation succeeded!")
    return "Success"


result = unstable_operation()
print("Result:", result)


def repeat_decorator(times=2):
    """
    Повторяет вызов функции указанное количество раз. /
    Repeats the function call a specified number of times.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat_decorator(times=3)
def say_hello():
    print("Hello!")


say_hello()
