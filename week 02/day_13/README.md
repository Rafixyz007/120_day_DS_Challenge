<h1 align="center">Day 13 Progress – File Handling & Serialization</h1> <h3 align="center"><b>Date: 17/01/2026</b></h3>
1️ The Safe Open

What we did:
Wrote to a file using a with statement so that it closes automatically without calling .close().

What we learned:
Context managers (with) ensure files are safely opened and closed, preventing resource leaks.

2️ Append vs Write

What we did:
Appended a new line to an existing file without overwriting old content.

What we learned:
Opening a file in append mode ('a') preserves existing content and adds new data at the end.

3️ Binary Mode

What we did:
Read an image file using binary mode ('rb') and printed its size.

What we learned:
Binary mode is necessary for non-text files. Reading in bytes prevents decoding errors.

4️ Encoding Hell

What we did:
Wrote text containing emojis using UTF-8 encoding.

What we learned:
Specifying UTF-8 encoding avoids UnicodeDecodeError and supports all Unicode characters.

5️ JSON Serialization

What we did:
Saved a Python dictionary to a JSON file using json.dump().

What we learned:
The json module allows easy serialization of Python objects for storage or transfer.

6️ CSV Parsing

What we did:
Created a CSV file using csv.DictWriter and read it back as a list of dictionaries with csv.DictReader.

What we learned:
CSV files can be easily handled as dictionaries, making data access intuitive in Python.

7️ Buffering

What we did:
Wrote 1 million lines to a file.

What we learned:
Python buffers file writes in memory, so the disk doesn’t physically write every single line immediately.

8️ Pathlib

What we did:
Safely joined folder and filename using pathlib.Path.

What we learned:
Path provides a cross-platform way to handle file paths on Windows, Mac, or Linux.

9️ Custom Context Manager

What we did:
Created a Timer context manager to measure execution time of a code block.

What we learned:
Custom context managers with __enter__ and __exit__ allow automatic setup and cleanup around code blocks.

10 Pickle (The Warning)

What we did:
Saved and loaded a Python object using pickle.

What we learned:
pickle can serialize Python objects for storage, but loading pickle files should be done carefully as it can execute arbitrary code.
