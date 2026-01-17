<h1 align="center">Day 13 Progress – File Handling & Serialization</h1>
<h3 align="center"><b>Date: 17/01/2026</b></h3>

---

## 1️ The Safe Open
**What we did:**  
Used a `with open()` block to write to a file without manually closing it.

**What we learned:**  
Python’s context manager automatically handles file closing, even if an error occurs, preventing resource leaks.

---

## 2️ Append vs Write
**What we did:**  
Added text to an existing file without deleting its previous content using append mode (`'a'`).

**What we learned:**  
Append mode preserves existing content while allowing new data to be added at the end of the file.

---

## 3️ Binary Mode
**What we did:**  
Opened and read an image file in binary mode (`'rb'`).

**What we learned:**  
Binary mode is required for non-text files like images, ensuring the data is read as raw bytes instead of text.

---

## 4️ Encoding Hell
**What we did:**  
Opened a text file in UTF-8 encoding and wrote emojis and special characters.

**What we learned:**  
Using the correct encoding (UTF-8) prevents `UnicodeDecodeError` and allows writing non-ASCII characters safely.

---

## 5️ JSON Serialization
**What we did:**  
Saved a Python dictionary to a file using the `json` module.

**What we learned:**  
`json.dump()` converts Python objects into JSON format and writes them to a file. Using `with` ensures safe file handling.

---

## 6️ CSV Parsing
**What we did:**  
Created a CSV file with `csv.DictWriter` and read it back into a list of dictionaries with `csv.DictReader`.

**What we learned:**  
- CSV files can be easily read and written as dictionaries for structured data.  
- Using `with` ensures files are properly opened and closed.

---

## 7️ Buffering
**What we did:**  
Wrote 1 million lines to a file.

**What we learned:**  
Writing large files doesn’t make the disk spin once per line due to buffering. Python writes data in chunks for efficiency.

---

## 8️ Pathlib
**What we did:**  
Safely joined folder and filename paths using `pathlib.Path`.

**What we learned:**  
`pathlib` provides a cross-platform way to handle file paths without worrying about OS-specific separators.

---

## 9️ Custom Context Manager
**What we did:**  
Created a `Timer` class to measure execution time of a code block using `with Timer():`.

**What we learned:**  
Custom context managers allow setup and cleanup operations for any block of code, following the `__enter__` and `__exit__` protocol.

---

## 10 Pickle (The Warning)
**What we did:**  
Serialized a Python object (class instance) to a file with `pickle.dump()` and loaded it back using `pickle.load()`.

**What we learned:**  
Pickle allows saving and restoring Python objects while preserving their state. Always use binary mode (`'wb'` / `'rb'`) for pickling.

---

## Summary
**What we did:**  
Explored writing, reading, appending files, handling encodings, working with JSON, CSV, large files, path manipulations, custom context managers, and object serialization with Pickle.

**What we learned:**  
- File handling is safe and efficient using context managers.  
- Encoding matters for text data.  
- Serialization (JSON, Pickle) allows persisting Python objects.  
- `pathlib` and custom context managers make code cleaner and more portable.
