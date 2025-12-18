## 1. Micro challenge: The speed Trap(Lookup)

## Goal: Create a list of 1 million numbers. create a set(hash table) of the same numbers. check if the number -1 exists in both.
## Constraint: you don't need to actually run 1M items, but explain why the set/dict is faster.

import time

list = []

for i in range(1,1000000+1): 
    list.append(i)  # creating list is faster



start_list_time = time.time()

# list = []

# for i in range(1,1000000+1):
#     list.append(i)

if -1 in list:  # searching list is slower
    print(True)
else:
    print(False)

end_list = time.time()
print(end_list - start_list_time)

# print(list)


my_set = set()

for i in range(1,1000000+1):
    my_set.add(i) # creating set is little bit slower than list


start_set_time = time.time()

# my_set = set()

# for i in range(1,1000000+1):
#     my_set.add(i)

# print(my_set)


if -1 in my_set: # searching list is way faster than list
    print(True)
else:
    print(False)

end_set = time.time()

print(end_set - start_set_time)


"""
Lists are faster to create because they store elements sequentially
without hashing.

For membership tests:
- `x in list` runs in O(n) time (linear search)
- `x in set` runs in O(1) average time (hash lookup)

So, lists are cheaper to build, while sets are much faster for searching.
"""