import time
import functools

# The goal of this function is to time a function

def timer(func):
    @functools.wraps(func) # preserves func's name/docstring

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "DONE"

slow_function()

# -> slow_function took 1.0001273155212402 seconds