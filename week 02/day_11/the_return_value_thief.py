## 4. Micro Challenge: The Return Value Thief

## Goal: Write a decorator that forgets to return func(*args). print the result of the decorated function.

def wrapper(func):
    def x(*args, **kwargs):
        func(*args, **kwargs)
    return x
    
    

@wrapper
def add(a,b):
    return a+b

result = add(2,3)
print(result)



"""
    Decorator that executes a function but discards its return value.

    The wrapped function is called with any provided positional and keyword
    arguments, but its return value is not returned to the caller. As a result,
    the decorated function always returns None, even if the original function
    returns a value.

    Parameters:
    func (callable): The function to decorate.

    Returns:
    callable: A wrapped function that forwards arguments to `func` but
    always returns None.
"""

