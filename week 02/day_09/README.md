<h1 align="center">Day 09 Progress - Generators</h1>
<h3 align="center"><b>Date: 09/01/2026</b></h3>

---

## 1️⃣ Micro Challenge: The Basic Yield
**What we did:** Created a generator that yields multiple values sequentially and iterated through it.  
**What we learned:** Generators produce values lazily and save memory; `yield` allows pausing and resuming a function.

---

## 2️⃣ Micro Challenge: The Memory Profile
**What we did:** Compared memory usage of a list comprehension versus a generator expression for 1 million numbers.  
**What we learned:** Generators are far more memory-efficient than lists because they produce values on the fly.

---

## 3️⃣ Micro Challenge: The Infinite Sequence
**What we did:** Built a Fibonacci generator that can produce numbers indefinitely.  
**What we learned:** Generators can implement infinite sequences efficiently, without consuming all memory.

---

## 4️⃣ Micro Challenge: The One-Time Trap
**What we did:** Attempted to iterate through a generator twice.  
**What we learned:** Generators can only be iterated once; after they are exhausted, they yield nothing.

---

## 5️⃣ Micro Challenge: The Next Protocol
**What we did:** Used `next()` to manually retrieve values from a generator.  
**What we learned:** `next()` allows controlled iteration and demonstrates how a generator maintains its state.

---

## 6️⃣ Micro Challenge: The Pipeline (Chaining)
**What we did:** Chained two generators: one for squaring numbers, one for filtering evens.  
**What we learned:** Generators can be composed to create memory-efficient data processing pipelines.

---

## 7️⃣ Micro Challenge: The Large File Reader
**What we did:** Created a generator to read a large file line by line.  
**What we learned:** Generators allow processing huge files efficiently without loading the entire file into memory.

---

## 8️⃣ Micro Challenge: Yield From
**What we did:** Combined multiple sub-generators using `yield from`.  
**What we learned:** `yield from` simplifies chaining generators and delegating iteration cleanly.

---

## 9️⃣ Micro Challenge: The Send Method
**What we did:** Built a generator that calculates the square of numbers sent using `send()`.  
**What we learned:** Generators can receive input dynamically via `send()`, enabling interactive and stateful computation.

---

## 🔟 Micro Challenge: State Retention
**What we did:** Created a generator to calculate the running average of sent numbers.  
**What we learned:** Generators maintain internal state across multiple `send()` calls, enabling continuous calculations like running averages.

