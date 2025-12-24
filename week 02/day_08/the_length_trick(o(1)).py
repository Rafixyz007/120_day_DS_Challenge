## 6. Micro Challenge: The Length Trick(o(1))

## Goal: call len() on a list of 1 billion items.

l = range(1000000000)  # range is memory-efficient
print(len(l))  # fast, O(1)


"""
Micro Challenge: The Length Trick (O(1))

Calling len() on a Python list or range is O(1) because the
length is stored internally. It does not depend on the size
of the list. Creating extremely large lists in memory is
not necessary to demonstrate this.
"""
