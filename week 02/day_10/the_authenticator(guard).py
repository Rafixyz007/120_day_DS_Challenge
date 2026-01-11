## 6. Micro Challenge: The Authenticator(Guard)

## Goal: Create @admin_required. if global USER != 'admin', raise PermissionError.


USER = input("enter user: ").upper()

def admin_required(func):
    def wrapper(*args, **kwargs):
        if USER != "admin":
            raise PermissionError
        return func(*args, **kwargs)
    return wrapper

@admin_required
def sensitive_func():
        print("access successfull")

sensitive_func()


"""
    Decorator that restricts function execution to admin users only.

    This decorator checks a global variable `USER` before allowing the
    decorated function to run. The comparison is case-sensitive and
    expects `USER` to match the admin identifier exactly.

    Raises:
    PermissionError: If USER is not authorized.
"""
