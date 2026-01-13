## 5. Micro Challenge: The Property Decorator

## Goal: Create a "fake" variable user.age that is


class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = 2026
        return current_year - self.birth_year


user1 = User("Mejbah bhai", 2000)


print(user1.age)
