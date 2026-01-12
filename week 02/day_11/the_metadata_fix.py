# ## 8. Micro Challenge: The Metadata Fix

# ## Goal: print func. __name__ of a decorated function.


from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_function():
    pass

print(my_function.__name__)
