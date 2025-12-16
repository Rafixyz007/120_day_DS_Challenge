## 3. Micro Challenge The efficient skipper

## Goal: Loop through numbers 1 to 10. print them, but if the number is 5, skip it and do not print anything.
## Constraint: Use the continue keyword.

for i in range(1,11):
    if i == 5:
        continue
    print(i)