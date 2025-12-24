## 9. Micro Challenge: The Dictionary Creator(O(N))

## Goal: Measure the time to create a dict from a list vs searching it.


import time

l = list(range(10000))


start_time = time.perf_counter()
d = {x: True for x in l}
end_time = time.perf_counter()
print("Building dict:", end_time - start_time)



start_list_search = time.perf_counter()
for x in l:
    if x in l:
        pass
end_list_search = time.perf_counter()
print("Searching in list:", end_list_search - start_list_search)



start_dict_search = time.perf_counter()
for x in l:
    if x in d:
        pass
end_dict_search = time.perf_counter()
print("Searching in dict:", end_dict_search - start_dict_search)


"""
Building a dictionary from a list costs O(n).
Dictionary lookups are O(1) on average, while list lookups are O(n).
Converting to a dict once is often faster than repeated list searches.
"""