## 1. Micro Challenge: The Linear Scan(o(N))

## Goal: Create a list of 10 million numbers. Check if -5 is in the list.


import time


million = []

for i in range(1,1000000+1):
    million.append(i)

start_list_time = time.time()

if -5 in million:
    print(True)
else:
    print(False)

end_list_time = time.time()
print(end_list_time - start_list_time)

