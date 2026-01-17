## 4. Micro Challenge: Encoding Hell

## Goal: Fix a "UnicodeDecodeError".

with open("text_with_emoji.txt", "w", encoding= "utf-8") as f:
    f.write("Emojis 🌱☀️ - Copy & Paste Online 🕵️‍♀️")


"""
Explanation:
    This code opens a text file in write mode ('w') with UTF-8 encoding,
    which supports all Unicode characters including emojis. Using the
    correct encoding prevents errors that occur when Python tries to write
    characters not supported by the default encoding (often ASCII). The
    text is safely written to the file, and the file is automatically closed
    when the block finishes.

Behavior:
    - Opens 'text_with_emoji.txt' in write mode with UTF-8 encoding.
    - Writes a string containing emojis and special characters.
    - Automatically closes the file when done.
    - Prevents UnicodeDecodeError when writing non-ASCII characters.
"""