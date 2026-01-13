## 6. Micro Challenge: Class Variables Vs Instance Variables

## Goal: Set species = "Human" on the Class. Set name = "A" on the Instance. Change species and see who is affected.


class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name


p1 = Person("A")
p2 = Person("B")

print(p1.species, p2.species)  

Person.species = "Animal"

print(p1.species, p2.species)


p1.species = "Robot"

print(p1.species)
print(p2.species)
print(Person.species)


"""

`species` is a class variable, so it is shared by all instances of the class.
Initially, both p1 and p2 access `species` from the Person class.

When `Person.species` is changed to "Animal", the change affects all instances
that do not have their own `species` attribute.

When `p1.species` is set to "Robot", Python creates an instance variable
named `species` for p1 only. This instance variable shadows the class variable.

"""