## 10. Micro Challenge: The Slice Copy(O(k))

## Goal: Slice a massive list data[0:5000].


import time

start_list_time = time.perf_counter()

data = list(range(100000))

end_list_time = time.perf_counter()
print("creating a list: ", end_list_time - start_list_time)

start_time = time.perf_counter()
slice_ = data[0:5000]
end_time = time.perf_counter()

print("time to slice 5000 items:", end_time - start_time)



"""
List slicing creates a new list by copying the requested elements.
The time complexity depends on the slice size (k), not the total
list size, making slicing an O(k) operation.
"""





