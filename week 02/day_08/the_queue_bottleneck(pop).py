## 4. Micro Challenge: The Queue Bottleneck(pop)

## Goal: Compare list.pop() vs list.(0)


import time

value = list(range(1,100+1))


start_time_index = time.perf_counter()

value.pop()

end_time_index = time.perf_counter()

print("pop without index: ", end_time_index - start_time_index )


start_time_with_index = time.perf_counter()


value.pop(0)

end_time_with_index = time.perf_counter()

print("pop with index: ", end_time_with_index - start_time_with_index)


'''
"""
Reason: Why pop() is faster than pop(index)

Python lists are implemented as dynamic arrays stored in contiguous memory.

pop()
- Removes the last element of the list.
- Requires no shifting of elements.
- Simply reduces the list size.
- Time complexity: O(1) (amortized).

pop(index)
- Removes an element at a specific position.
- Requires index validation and extra internal checks.
- If the index is not the last position, all subsequent elements
  must be shifted left to fill the gap.
- Time complexity: O(n) in the general case.

Conclusion:
pop() is faster than pop(index) because it performs less work
and avoids element shifting.
"""

'''