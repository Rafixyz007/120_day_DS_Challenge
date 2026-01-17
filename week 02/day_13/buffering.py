## 7 Micro Challenge: Buffering

## Goal: Write a 1 million lines. Why doesn't the disk spin 1 million times?


with open("buffer.txt", "w") as f:
    for i in range(1000000):
        f.write("Why dosen't the disk spin 1 million times?\n")
        