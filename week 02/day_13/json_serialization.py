## 5. Micro challenge: JSON Serialization

## Goal: Save a dictionary to a file.

import json

d = {"a":1, "b":2}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(d, f)


"""
Explanation:
    This code uses Python’s built-in `json` module to serialize a dictionary
    and write it to a file. By opening the file in write mode ('w') with UTF-8
    encoding, it ensures that all characters are correctly handled. The 
    `json.dump()` function converts the dictionary into JSON format and writes
    it directly to the file. Using a `with` statement ensures that the file is
    automatically closed after writing, preventing resource leaks.

Behavior:
    - Opens 'data.json' in write mode with UTF-8 encoding.
    - Serializes the dictionary {"a":1, "b":2} into JSON format.
    - Writes the JSON data to the file.
    - Automatically closes the file when the block finishes.
"""