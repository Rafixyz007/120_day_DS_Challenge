## 8. Micro Challenge: The Super Proxy

## Goal: Override __init__ in Admin. but still run the User setup.


class User:
    def __init__(self, name):
        self.name = name
        print("User initialized")


class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        print("Admin initialized")


a = Admin("Root", 10)
