## 3. Micro Challenge: Binary Mode.

## Goal: Read an image file.



with open("2.png", "rb") as f:
    data = f.read()
    print(len(data))


"""
Explanation:
    This code opens an image file using binary read mode ('rb'), which is
    required for non-text files such as images. The entire file is read as
    raw bytes and stored in memory. Printing the length of the byte sequence
    confirms that the file was successfully read without attempting to
    display or interpret the binary data.

Behavior:
    - Opens '2.png' in binary read mode.
    - Reads the complete file into a bytes object.
    - Prints the total number of bytes in the image.
    - Automatically closes the file when the block exits.
"""


