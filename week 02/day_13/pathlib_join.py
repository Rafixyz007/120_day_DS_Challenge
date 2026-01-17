## 8. Micro Challenge: Pathlib

## Goal: Join a folder and filename safely on windows and mac.


from pathlib import Path

pathlib_concate = Path("pathlib_folder") / "pathlib.txt"

print(pathlib_concate)