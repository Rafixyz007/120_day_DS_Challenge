## 9. Micro Challenge: Custom Context Manager

## Goal: Create a block with Timer(): that prints time taken


import time

class Timer:
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, *args):
        print("Time taken:", time.time() - self.start)


with Timer():
    sum(range(1000000))



    """
    A custom context manager to measure execution time of a code block.
    
    Usage:
        with Timer():
            # code to time
            do_something()
    
    Behavior:
        - __enter__: records start time
        - __exit__: calculates and prints elapsed time
    """
