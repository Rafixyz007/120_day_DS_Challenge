## 2. Micro Challenge: The Accumulator Pattern

## Goal: Ask the user for a number N (e.g.,5). calculate the sum of all numbers from 1 to N (1+2+3+4+5)
## Constraint: Do not use the math formula n(n+1)/2. you must use a for loop and a tracker variable.


user = int(input("Enter a number: "))

total = 0
for i in range(1, user + 1):
    total = total + i
print(f"The sum of numbers from 1 to {user} is: {total}")