## 1. Micro challenge The Infinite Guardian

## Goal: Write a script that asks the user for a password repeatedly. it must run forever until the user types "Stop"
## Constraint: Use while True and handle the exit condition manually.


while True:
    pwd = input("Enter a password: ").strip().lower()
    if pwd == "stop":
        break