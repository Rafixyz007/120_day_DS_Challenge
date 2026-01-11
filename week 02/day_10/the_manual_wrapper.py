## 1. Micro Challenge: The Manual Wrapper

## Goal: write a function wrapper(func) that runs code before/after func. Apply it manually: new_func = wrapper(old_func).

def wrapper(func):
    def x():
        print('before calling')
        func()
        print('after calling')
    return x

def old_func():
    print("old function")

new_func = wrapper(old_func)

new_func()



"""
    Wraps a function to execute code before and after calling it.

    Parameters:
    func (callable): The function to be wrapped.

    Returns:
    callable: A new function that, when called, prints 'before calling',
              executes the original function, and then prints 'after calling'.

    Example:
    >>> def old_func():
    ...     print("old function")
    >>> new_func = wrapper(old_func)
    >>> new_func()
    before calling
    old function
    after calling
"""