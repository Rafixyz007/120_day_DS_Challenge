## 7. Micro Challenge: The Memoizer(Cache)

## Goal:  Write a @cache decorator that stores results of expensive function calls in a dictionary.


def cache(func):
    values = {}
    def wrapper(*args, **kwargs):
        key = (args,tuple(sorted(kwargs.items())))
        if key in values:
            return values[key]
        result = func(*args, **kwargs)
        values[key] = result
        return result
    return wrapper

@cache
def add(a,b):
    print(f"adding {a} + {b}")
    return a+b

print(add(2,5))
print(add(2,5))
