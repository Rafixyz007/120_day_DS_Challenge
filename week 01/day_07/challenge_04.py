## 4. Micro Challenge: The Custom Signal

## Goal: Ask the user for a number. if the number negative, manually trigger an error using raise ValueError("No Negatives")


user = int(input("Enter a number: "))

if user < 0:
    raise ValueError("No Negatives")