## 3. Micro Challenge: The Stack Emulator

## Goal: create an empty list. add number 1,2,3. then remove the last number(3) and print it.
## constraint: use .append() and .pop(). do not use insert() or remove().


list = []

list.append(1)
list.append(2)
list.append(3)
print(list,"\n")
x = list.pop()
print(f"last element is deleted from the list using .pop()\n{x}")



