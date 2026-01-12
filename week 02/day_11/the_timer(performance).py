## 5. Micro Challenge: The Timer(Performance)

## Goal: Create a @timer decoator that prints execution time using time.time()

import time

def timer(func):
    def x(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("execution time:",end - start)
        return result
    return x

@timer
def add(a,b):
    return a+b

add(2,3)


"""
    Decorator that measures and prints the execution time of a function.

    This decorator uses time.time() to record the start and end times
    of the function call, and prints the elapsed time in seconds.
    The return value of the original function is preserved.

    Parameters:
    func (callable): The function to be decorated.

    Returns:
    callable: A wrapped function that prints execution time and returns
    the original function's result.

"""
