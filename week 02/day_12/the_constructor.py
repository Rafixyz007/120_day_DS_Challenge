## 1. Micro Challenge: The Constructor


## Goal: Create a class user. Ensure every user start with is_active = True.

class User:

    """
    Represents a user in the system.

    Every User instance is initialized in an active state
    by default. The `is_active` attribute is set to True
    when the object is created.
    """
        
    def __init__(self):
        self.is_active = True



u1 = User()
u2 = User()

print(u1.is_active)
print(u2.is_active)


