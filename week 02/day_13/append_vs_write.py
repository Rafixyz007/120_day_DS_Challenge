## 2. Micro Challenge: Append vs Write

## Goal: Add a long line without deleting old content.


with open("test.txt", "a") as f:
    f.write("\nIn Sha Allah i am going to complete 120 day challenge ")


"""
Explanation:
    This code opens the file in append mode ('a'), which ensures that any
    new text is added to the end of the file instead of overwriting it.
    Unlike write mode ('w'), append mode preserves all previous content.

Behavior:
    - Opens 'test.txt' in append mode.
    - Adds a new line at the end of the file.
    - Keeps all existing file content unchanged.
    - Automatically closes the file when the block exits.
"""