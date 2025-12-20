## 2. Micro Challenge: The Math Safety Net

## Goal: create a variable x = 0. Try to print 100/x. Catch the specific error that occurs.


x = 0 

try:
    100/x

except ZeroDivisionError as z:
    print(z)