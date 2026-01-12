<h1 align="center">Day 11 Progress – Functional Programming</h1>
<h3 align="center"><b>Date: 12/01/2026</b></h3>

---

## 1️ The Anonymous Function
**What we did:**  
Created simple arithmetic functions (add, subtract, multiply, divide) using `lambda`.

**What we learned:**  
Lambda expressions provide a concise way to define small, single-expression functions.

---

## 2️ The Mapper
**What we did:**  
Used `map()` to square each number in a list.

**What we learned:**  
`map()` applies a function to all items in an iterable, returning a new iterator.

---

## 3️ The Filter
**What we did:**  
Removed negative numbers from a list using `filter()`.

**What we learned:**  
`filter()` selectively keeps elements that satisfy a condition, making data cleaning straightforward.

---

## 4️ The Reducer
**What we did:**  
Calculated the product of a list using `functools.reduce()`.

**What we learned:**  
`reduce()` aggregates an iterable to a single value by applying a binary function repeatedly.

---

## 5️ The Custom Sort Key
**What we did:**  
Sorted strings like "100px", "20px", "3px" numerically by extracting numeric values.

**What we learned:**  
Custom sort keys allow fine-grained control over sorting behavior for non-standard data.

---

## 6️ The Zip Lock
**What we did:**  
Combined two lists (`names` and `ages`) into a dictionary using `zip()`.

**What we learned:**  
`zip()` pairs elements from multiple iterables, and `dict()` can convert these pairs into a dictionary efficiently.

---

## 7️ List Comprehension vs Map/Lambda
**What we did:**  
Compared performance of squaring numbers using `map(lambda…)` versus list comprehension.

**What we learned:**  
List comprehensions are usually more readable and often perform slightly better than `map` with `lambda` for simple operations.

---

## 8️ Any and All
**What we did:**  
Checked if any numbers were negative and if all numbers were positive using `any()` and `all()`.

**What we learned:**  
Built-in functions `any()` and `all()` provide concise ways to check conditions across an iterable.

---

## 9️ Partial Functions
**What we did:**  
Created a general `power(base, exp)` function and specialized it into a `square(x)` using `functools.partial`.

**What we learned:**  
`partial()` allows pre-setting some arguments of a function, creating reusable specialized versions easily.

---

## 10 Immutability Test
**What we did:**  
Tried to modify a tuple inside a `map()` function.

**What we learned:**  
Tuples are immutable; operations like `map()` require creating a new tuple instead of modifying the original.

---

##  Key Takeaways
- Lambdas simplify small, one-line functions.
- `map`, `filter`, `reduce` enable functional-style programming.
- Custom sort keys and `zip` enhance data manipulation.
- `any` and `all` make condition checks concise.
- `functools.partial` allows function specialization.
- Tuples are immutable; always return a new object when “modifying” them.

