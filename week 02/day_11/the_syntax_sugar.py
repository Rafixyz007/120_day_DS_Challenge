## 2. Micro Challenge: The Syntax Sugar

## Goal: Apply the wrapper using the @decorator syntax.


def wrapper(func):
    def x():
        print("before calling")
        func()
        print("after calling")
    return x

@wrapper
def old_func():
    print("this is an old function")

old_func()


"""
    Decorator that wraps a function to run code before and after it executes.

    The returned function prints a message before calling the original function,
    then calls it, and finally prints a message after execution.

    Parameters:
    func (callable): The function being decorated.

    Returns:
    callable: A wrapped version of the original function with pre- and post-
    execution behavior.
"""
