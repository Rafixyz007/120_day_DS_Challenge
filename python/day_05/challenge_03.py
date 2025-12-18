## 3. Micro Challenge: The frequency counter

## Goal: input a string "banana". create a dictionary that counts the frequency of each letter (e.g., {"b":1, "a":3, "n":2}).
## Constraint: use a standard for loop and if/else logic.

string = "banana"
my_dict = {}

for char in string:
    if char in my_dict:
        my_dict[char] = my_dict[char] + 1
    else:
        my_dict[char] = 1

print(my_dict)
