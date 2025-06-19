import time
import functools


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Измеряет время выполнения функции и выводит результат /
        Measures the execution time of a function and prints the result.
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds.")
        return result

    return wrapper


@timeit
def sum_numbers(numbers):
    return sum(numbers)


result = sum_numbers(range(1000000))
print(result)


def only_once(func):
    has_run = {"value": False}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Выполняет функцию только один раз. При повторных вызовах выводит предупреждение. /
        Executes the function only once. Prints a warning on subsequent calls.
        """
        if not has_run["value"]:
            has_run["value"] = True
            return func(*args, **kwargs)
        print(f"Function: {func.__name__} has already been executed.")
    return wrapper


@only_once
def initialize_database():
    print("Инициализация базы данных...")

initialize_database()
initialize_database()