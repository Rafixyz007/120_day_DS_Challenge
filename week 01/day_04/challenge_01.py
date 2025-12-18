## 1. Micro Challenge: The Reference Trap

## Goal: create a list a = [1,2,3]. set b = a. change the first item of b to 99. print a.
## observation: a also changes to [99,2,3]


a = [1, 2, 3]
b = a
b[0] = 99

print('This is "a" set in a reference trap')
print(a)

# Fix
a = [3, 2, 1]
b = a.copy()
b[0] = 99

print("After fixing with copy()")
print(a)
