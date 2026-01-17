## 1. Micro Challenge: The Safe Open


## Goal: Write to a file without .close().


with open("test.txt", "w") as f:
    f.write("This is day 13 of 120 day ML/DL challenge!")


"""
Explanation:
    This code uses Python’s context manager (`with` statement) to safely
    open a file in write mode. The file is automatically closed when the
    block finishes execution, even if an error occurs. This prevents
    resource leaks and is the recommended way to handle files in Python.

Behavior:
    - Opens (or creates) 'test.txt' in write mode.
    - Writes a single line of text to the file.
    - Automatically closes the file after writing.
"""