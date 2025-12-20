## 1. Micro Challenge: The Input Guard

## Goal: Write a script that asks the user for their age. if they text print "Numbers only" instead of crashing.
## Constraint: Use try/except ValueError.


try:
    age = int(input("enter your age: "))

except ValueError:
    print("Numbers only")



