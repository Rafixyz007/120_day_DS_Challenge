## 10. Micro Challenge: Decorators With Arguments


## Goal: Create a decorator that accepts a setting: @repeat(time=3).


def repeat(time):

    """
    A decorator factory that repeats execution of a function.

    Parameters
    ----------
    time : int
        Number of times the decorated function should be executed
        each time it is called.

    Returns
    -------
    decorator : function
        A decorator that wraps a function so it runs `time` times.
    """

    def decorator(func):


        """
        Decorates a function to repeat its execution.

        Parameters
        ----------
        func : function
            The function to be wrapped.

        Returns
        -------
        wrapper : function
            A wrapped version of `func` that executes it multiple times.
        """


        def wrapper(*args, **kwargs):

            """
            Executes the wrapped function repeatedly.

            Accepts any positional and keyword arguments and
            forwards them to the original function.
            """
                        
            for _ in range(time):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def f(name):
    print(f"Hello {name}")

f("world")

