## 9. Micro Challenge: The Stacked Decorator

## Goal: Apply two decorators: @bold and @italic to a string returning function.



def bold(func):

    """
        Decorator that wraps the return value of a function with
        bold-style markers before and after the original output.

        This decorator demonstrates how an outer decorator executes
        after inner decorators in a stacked decorator setup.
    """
    def wrapper():
        return f"[bold 1st]{func()}[bold last]"
    return wrapper


def italic(func):

    """
    Decorator that wraps the return value of a function with
    italic-style markers before and after the original output.

    When stacked with other decorators, this decorator executes
    first if placed closest to the function definition.
    """

    def wrapper():
        return f"[italic 1st]{func()}[italic last]"
    return wrapper


@bold
@italic
def msg():

    """
    Returns a string to demonstrate the execution order of
    stacked decorators (inner to outer).

    The function output is first modified by the inner decorator
    and then by the outer decorator.
    """
    
    return "before and after"

print(msg())





