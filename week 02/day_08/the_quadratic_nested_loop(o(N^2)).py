## 7. Micro Challenge: The Quadratic Nested Loop(o(N^2))

## Goal: Find duplicates between two lists using nested for loops. for every item in list a, you scan all items in list b. 10000*10000 = 100000000 operations, this is the most common cause of server timeout


import time

a = list(range(10000+1))
b = list(range(10000+1))

start_list_time = time.perf_counter()


for item_a in a:
    for item_b in b:
        if item_a == item_b:
            # print(True)
            break

end_list_time = time.perf_counter()

print("time for list: ", end_list_time - start_list_time)


