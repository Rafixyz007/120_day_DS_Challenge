## 6. Micro Challenge: CSV Parsing

## Goal: Read a CSV into a list of dictionaries.

import csv


with open("data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["a","b"])
    writer.writeheader()
    writer.writerow({"a": "Intelligence", "b": "Academy"})
    writer.writerow({"a": "120 days", "b": "ML/DL Challenge"})


with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)


"""
Explanation:
    This script first creates a CSV file using `csv.DictWriter` to simulate
    a CSV with headers and rows. Then it reads the CSV file using `csv.DictReader`,
    which interprets each row as a dictionary using the first row as keys.
    Converting the reader to a list collects all rows into a list of dictionaries.
    This approach ensures that CSV data is easily accessible as Python dictionaries,
    and the `with` statements guarantee that files are safely opened and closed.

Behavior:
    - Writes a CSV file named 'data.csv' with two rows of sample data.
    - Reads the CSV file into a `DictReader` object.
    - Converts the `DictReader` into a list of dictionaries.
    - Prints the resulting list.
"""

