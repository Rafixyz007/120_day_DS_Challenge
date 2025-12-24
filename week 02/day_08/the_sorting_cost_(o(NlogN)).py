## 8. Micro Challenge: The Sorting Cost(O(NlogN))


## Goal: Sort a random list

import time


num = [1,4,6,3,1,9,87,54,24,5,43,1,34,6,78,766,543,233,421,56,35,2,24,63,5]

start_time = time.perf_counter()

num.sort()

end_time = time.perf_counter()

print("Takes time to sort without loop: ", end_time - start_time)

start_time_in_loop = time.perf_counter()

for _ in num:
    num.sort()
end_time_in_loop = time.perf_counter()

print("Takes time to sort inside in loop: ", end_time_in_loop - start_time_in_loop)
