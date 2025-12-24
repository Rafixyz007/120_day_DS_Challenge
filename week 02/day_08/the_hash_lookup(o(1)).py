## 2. Micro Challenge: THe Hash Lookup(0(1))


## Goal: Convert that list to a set. Check for -5 again.

import time

million_list = []

for i in range(1,10000000+1):
    million_list.append(i)

million_set = set(million_list)

start_time = time.time()

if -5 in million_set:
    print(True)

else:
    print(False)

end_time = time.time()
print(end_time - start_time)