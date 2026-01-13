## 4. Micro Challenge: Private Variables


## Goal: Prevent external code from changing user.password.

class User:
    def __init__(self, password):
        self.__password = password


u = User("1234")
print(u.__password)


"""
By defining the password as a private variable with double underscores
(self.__password), Python hides it from external access using name mangling.
Any attempt to access u.__password directly will raise an AttributeError,
ensuring that the password cannot be modified from outside the class.

"""