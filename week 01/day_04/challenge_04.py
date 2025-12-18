## 4. Micro Challenge: The One-Line Architect

## Goal: create a list of numbers from 1 to 10. generate a new list containing the squares of only the even numbers.
## Constraint: Do this in exactly one line using  List comprehension.

numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [x**2 for x in numbers if x % 2 == 0]
print(f"This prints the squares of all even numbers from 1 to 10. {squares}")