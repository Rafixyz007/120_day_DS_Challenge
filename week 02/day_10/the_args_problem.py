## 3. Micro Challenge: The Args Problem

## Goal: Try to decorate a function that takes arguments add(a,b) with a wrapper that takes none.

def wrapper(func):
    def x():
        print("it takes none")
        return func()
    return x

@wrapper
def add(a,b):
    print(a+b)

add(2,3)


"""
    Decorator that wraps a function with a no-argument wrapper.

    This decorator is intentionally incorrect for functions that require
    positional arguments. The returned wrapper function takes no parameters
    and calls the original function without arguments.

    When applied to a function like `add(a, b)`, calling the decorated
    function will raise a TypeError because the required arguments are
    not passed through.

    Parameters:
    func (callable): The function to decorate.

    Returns:
    callable: A wrapper function that takes no arguments.
    """



