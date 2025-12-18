## 2. Micro Challenge: The Slicing Surgeon

## Goal: Create a list data = [10,20,30,40,50]. create a new list containing the last 3 items in reverse order.
## Constraint: Use Slicing syntax[start:stop:step].

data = [20,30,40,50]

a = data[:0:-1]
print(a)
print(data)