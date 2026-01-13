## 7. Micro Challenge: Inheritance


## Goal: Create Admin(User). Add a method delete_db() only for Admin.


class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print("User logged in")


class Admin(User):
    def delete_db(self):
        print("Database deleted")


a = Admin("Root")
a.login()
a.delete_db()
