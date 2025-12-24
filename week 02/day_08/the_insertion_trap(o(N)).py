## 3. Micro Challenge: The Insertion Trap(o(N))

## Goal: Compare list.append(x) vs list.insert(0,x)


import time

million = []

for i in range(1,1000000+1):
    million.append(i)

start_time_append = time.perf_counter()

million.append(10)

end_time_append = time.perf_counter()

print("append time:", end_time_append - start_time_append)


start_time_insert = time.perf_counter()

million.insert(0,11)

end_time_insert = time.perf_counter()

print("insert time:",end_time_insert - start_time_insert)