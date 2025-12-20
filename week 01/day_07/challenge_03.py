## 3. Micro Challenge: The Cleanup Crew

## Goal: Write a try/except block that divides two numbers. add a finally block that print "Execution Complete" Regardless of whether the division succeeded or failed.


try:
    number_1 = int(input("enter 1st number: "))
    number_2 = int(input("enter 2nd number: "))

    division = number_1/number_2
    print(division)

except Exception as e:
    print(e)
finally:
    print("Execution Complete")