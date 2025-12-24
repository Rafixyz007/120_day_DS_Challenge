# ## 5. Micro Challenge: The String Builder(0(N^2))

# ## Goal: Loop 10000 times and add a character to a string using s += "a"

import time


start_time_s = time.perf_counter()

s = ""

for char in range(1,10000+1):

    s += "a"

end_time_s = time.perf_counter()
print('without "".join: ', end_time_s - start_time_s)


## Fix using "".join()


start_time_l = time.perf_counter()

l = []

for char in range(1,10000+1):

    l.append("a")
s2 = "".join(l)

end_time_l = time.perf_counter()

print('with "".join: ', end_time_l - start_time_l)



"""
Compare string building methods:

- s += "a": slow (O(n^2)) due to repeated copying.
- list + join: fast (O(n)) by accumulating in a list and joining once.
"""
