## 3. Micro Challenge: The String Representation

## Goal: Make print(user) show "User: [Name]" instead of memory address.


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"


u = User("Alice")

print(u)
print([u])


"""
This demonstrates how to customize the string output of objects.

- __str__: Returns a human-readable string for end users.
           Called by print() or str().
           Example: print(u) -> "User: Alice"

- __repr__: Returns a developer-friendly string for debugging.
            Called in interactive displays or when the object appears in a list.
            Example: [u] -> [User(name='Alice')]

Overriding these methods gives your objects a clear “voice” both
for users and developers.

"""